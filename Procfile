web: python manage.py collectstatic --noinput
release: python manage.py migrate
web: gunicorn artsrec.wsgi --log-file=-