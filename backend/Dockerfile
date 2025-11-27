# https://www.docker.com/blog/how-to-dockerize-django-app/

# Stage 1: Base build stage
FROM python:3.14-slim AS builder

# .pyc files won't be written. The container's filesystem won't get modified at runtime and can therefore be read only.
# https://stackoverflow.com/questions/59732335/is-there-any-disadvantage-in-using-pythondontwritebytecode-in-docker
ENV PYTHONDONTWRITEBYTECODE=1
#  Python output (stdout and stderr) streams are sent straight to terminal without being first buffered
# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONUNBUFFERED=1

# Create the app directory
RUN mkdir /app

# Set the working directory in the container
WORKDIR /app

# # Install system dependencies, netcat added for entrypoint script
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version BEFORE installing requirements
RUN pip install --upgrade pip 
# Copy the requirements file first to leverage Docker's layer caching. 
# Only reinstall if there are changes to requirements.txt
COPY requirements.txt /app/
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt



# Stage 2: Production stage
# Use a clean, slim image for runtime server
FROM python:3.14-slim

# Create a non-root user and set permissions
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

# Copy only the built Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.14/site-packages/ /usr/local/lib/python3.14/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Install the PostgreSQL client and Netcat directly in the final image
# This is a much more reliable approach than copying from another image
RUN apt-get update && apt-get install -y \
    postgresql-client \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application code with non-root user permissions
COPY --chown=appuser:appuser . .

# Set environment variables to optimize Python and assist with debugging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Switch to the non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Copy the entrypoint script and make it executable
COPY --chown=appuser:appuser ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
