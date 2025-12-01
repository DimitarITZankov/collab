FROM python:3.11-slim
LABEL maintainer="collab"

ENV PYTHONUNBUFFERED=1
ENV PATH="/py/bin:$PATH"

# Copy the requirements for caching
COPY ./requirements.txt /tmp/requirements.txt

# Create Virtual Environment and install the Python packages
RUN python -m venv /py && \
	/py/bin/pip install --upgrade pip && \
	/py/bin/pip install -r /tmp/requirements.txt && \
	rm -rf /tmp

# Copy the app code and set working directory
COPY ./app /app
WORKDIR /app

# Create non-root user and set the ownership
RUN adduser --disabled-password --no-create-home django-user && \
	chown -R django-user /app

# Expose the port 
EXPOSE 8000

# Swtich to the non-root user
USER django-user

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]