#!/bin/sh

python manage.py makemigrations --noinput && \
python manage.py migrate --noinput && \
python manage.py collectstatic --noinput && \
python manage.py createsuperuser --noinput;
gunicorn config.wsgi -b 0.0.0.0:8000