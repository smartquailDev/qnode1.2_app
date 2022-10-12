#!/bin/sh

set -e
neofetch --ascii qnode_art.txt --ascii_colors 2 222 2 2 2 -L, --logo && \
go get github.com/mailhog/mhsendmail && \
cp /root/go/bin/mhsendmail /usr/bin/mhsendmail && \
#echo 'sendmail_path = /usr/bin/mhsendmail --smtp-addr mailhog:1025' > /usr/local/etc/php/php.ini

APP_PORT=${PORT:-9000}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"smartquail.info@gmail.com"}


python manage.py migrate --noinput
python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
python manage.py collectstatic --noinput 
django-admin makemessages --all
django-admin compilemessages 


uwsgi  --socket :9000 --workers 4 --master --enable-threads --module qnode12_app.wsgi --ini uwsgi_prod.ini

#python manage.py listen_port25 --noinput

#gunicorn --worker-tmp-dir /dev/shm  --bind "0.0.0.0:${APP_PORT}"  qnode0_app.wsgi:application 

