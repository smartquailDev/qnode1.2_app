FROM nginx:1.23.0-alpine

COPY ./nginx/* /etc/nginx/
COPY ./nginx/run.sh /run.sh
COPY ./islafloreana.com/* /etc/letsencrypt/live/islafloreanagalapagos.com


ENV LISTEN_PORT=80
ENV NGINX_PROXY=http://qnode12_app:9000
ENV APP_HOST=qnode12_app
ENV APP_PORT=9000

USER root

RUN apk add --no-cache openssl bash
RUN chmod +x /run.sh

RUN mkdir -p /qnode1.2_app/qnode12_app/staticfiles && \
    chmod 755 /qnode1.2_app/qnode12_app/staticfiles && \
    mkdir -p /qnode1.2_app/qnode12_app/mediafiles && \
    chmod 755 /qnode1.2_app/qnode12_app/mediafiles && \
    mkdir -p /qnode1.2_app/qnode12_app/media && \
    chmod 755 /qnode1.2_app/qnode12_app/media 

VOLUME /qnode1.2_app/qnode12_app/staticfiles
VOLUME /qnode1.2_app/qnode12_app/mediafiles
VOLUME /vol/www
VOLUME /vol/proxy
VOLUME /etc/letsencrypt

CMD ["/run.sh"]