web: python manage.py migrate && python manage.py ensure_admin && python manage.py collectstatic --noinput && gunicorn LionHeart.wsgi --bind 0.0.0.0:$PORT --workers 3 --timeout 120
