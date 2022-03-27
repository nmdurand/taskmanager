FROM python:3.6-stretch

RUN mkdir -p /var/www/app
WORKDIR /var/www/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

ENV FLASK_ENV=development
ENV FLASK_APP "app"

ENV DATABASE_SCHEME "sqlite://"
ENV DATABASE_PATH "/var/www/"
ENV DATABASE_NAME "taskmanager.db"

ENTRYPOINT flask run --host=0.0.0.0
