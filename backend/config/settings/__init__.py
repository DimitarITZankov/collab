import os

env = os.environ.get("DJANGO_ENV").lower()

if env == "prod":
    from .prod import *
else:
    from .dev import *