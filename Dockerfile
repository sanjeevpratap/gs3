FROM python:3.10-slim-buster



RUN mkdir /app1

WORKDIR /app1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV DJANGO_SETTING_MODULE=gs3.setting

ENV REDIS_URL=redis://redis-18739.c212.ap-south-1-1.ec2.cloud.redislabs.com:18739/

EXPOSE 8000

CMD daphne -b 0.0.0.0 -p 8000 gs3.asgi:application

