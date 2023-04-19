server {
    listen 80;
    server_name ${DOMAIN} www.${DOMAIN} 143.110.227.217 127.0.0.1;

    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }

    location /static {
    alias /qnode1.2_app/qnode12_app/staticfiles;
    client_max_body_size    1000M;
     }

    location /media {
    alias  /qnode1.2_app/qnode12_app/media;
    client_max_body_size    1000M;
     }

    location / {
        return 301 https://$host$request_uri;
    }
}

