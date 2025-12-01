# What's Gunicorn ?
	- This is Python WSGI HTTP server. WSGI is the standart for Python web apps like Django/Flask to talk to a web server. It's used in production, instead of the default 'runserver' used for development

# What does pre-forker mean ?
	- Gunicorn uses pre-fork worker model. The server starts multiple worker processes ahead of time to handle requests
	1. Gunicorn (the master process) starts
	2. It forks multiple worker processes immediately (copies itself into separate processes)
	3. Each worker process can handle HTTP requests independently
	- We use pre-fork because :
	1. Multiple requests can be served at the same time
	2. Pre-forking avoids creating a new process for every request (which is slow)
	3. If one worker crashes, others continue serving
	! Guincorn creates multiple worker processes in advance to handle multiple requests at once. It's faster and safer than starting a new process for every request

