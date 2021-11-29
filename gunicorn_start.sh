#! /bin/bash

## cd /app
exec gunicorn -b :5000 --access-logfile - --error-logfile - wsgi:app
