FROM python:3.9-alpine3.13
LABEL maintainer="smartquail.io"

ENV PYTHONUNBUFFERED 1




RUN apk add --no-cache git
ARG username=smartquailDev
ARG password=ms1719183830
RUN git clone https://github.com/smartquailDev/qnode1.2_app.git

#COPY . /qnode0_app
#COPY ./qnode0_app.dev/qnode0_app_env_dev/qnode0_app/ /qnode0_app
COPY ./requirements.txt /requirements.txt
COPY ./scripts /scripts
COPY ./uwsgi_prod.ini /qnode1.2_app/qnode12_app/uwsgi_prod.ini

#COPY ./.env /qnode0.1_app/qnode01_app/.env 
#No olvidar sacar las variables de entorno.


WORKDIR /qnode1.2_app/qnode12_app/
EXPOSE 443 
EXPOSE 25
EXPOSE 9000
EXPOSE 587

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps && \
    apk add build-base  postgresql-dev gcc musl-dev python3-dev linux-headers && \
    apk add libffi-dev build-base py3-cffi py3-cryptography && \
    apk add jpeg-dev   zlib-dev libjpeg build-base  wget  && \
    apk --update --upgrade --no-cache add fontconfig ttf-freefont font-noto terminus-font && \
    apk add gtk+3.0 pango && \
    apk del libressl-dev && \
    apk add busybox-extras && \
    apk add openssl-dev && \
    apk add gettext && \
    #/py/bin/pip install  rust  &&  \
    #/py/bin/pip install   py3-kiwisolver &&  \
    /py/bin/pip install -r /requirements.txt && \
    apk del openssl-dev  &&  \
    apk add libressl-dev  && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home qnode12 && \

    #Static Files
    mkdir -p /qnode1.2_app/qnode12_app/static && \
   # mkdir -p /qnode0.0_app/qnode0_app/static/media && \
    chmod -R 755 /qnode1.2_app/qnode12_app/static  && \

    mkdir -p /qnode1.2_app/qnode12_app/media && \
    chmod -R 755 /qnode1.2_app/qnode12_app/media  && \
    chown -R qnode12:qnode12 /qnode1.2_app/qnode12_app/media && \
    
    mkdir -p /qnode1.2_app/qnode12_app/staticfiles && \
    chmod -R 755 /qnode1.2_app/qnode12_app/staticfiles  && \
    chown -R qnode12:qnode12 /qnode1.2_app/qnode12_app/staticfiles && \

    #chmod -R 755 /qnode0.0_app/qnode0_app/static/media  && \
    chown -R qnode12:qnode12 /qnode1.2_app/qnode12_app/static && \
    #chown -R qnode0:qnode0 /qnode0.0_app/qnode0_app/static/media && \
    #Uswgi
    
    mkdir -p  /var/log/uwsgi/ && \
    chown -R qnode12:qnode12 /var/log/uwsgi/ && \
    #GNUCORN
    mkdir -p /qnode1.2_app/qnode12_app/run/ && \
    mkdir -p /var/log/gunicorn &&\
    chown -R qnode12:qnode12 /var/log/gunicorn &&\
    
    chmod -R 755 /qnode1.2_app/qnode12_app/ && \
    
    chmod -R 755 /scripts  && \
    chown -R qnode12:qnode12 /qnode1.2_app/qnode12_app/run/  && \
    chown -R qnode12:qnode12 /qnode1.2_app/qnode12_app/ &&\
    chmod -R 755 /var/log/gunicorn  && \
    
    #chmod -R u+x /scripts/gunicorn_run.sh &&\
    chmod -R u+x /scripts/run.sh &&\
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"
#COPY ./scripts/gunicorn.socket /qnode0.0_app/qnode0_app/run/



# Install language pack
RUN apk --no-cache add ca-certificates wget && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.25-r0/glibc-2.25-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.25-r0/glibc-bin-2.25-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.25-r0/glibc-i18n-2.25-r0.apk && \
   # apk add glibc-bin-2.25-r0.apk glibc-i18n-2.25-r0.apk glibc-2.25-r0.apk

COPY ./locale.md /locale.md
RUN cat locale.md | xargs -i /usr/glibc-compat/bin/localedef -i {} -f UTF-8 {}.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

USER qnode12

CMD ["run.sh"]


