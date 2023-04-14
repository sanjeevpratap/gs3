FROM python:3.10-slim-buster

# FROM alpine:latest

# RUN  apk add -update redis




RUN mkdir /app1

WORKDIR /app1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV DJANGO_SETTING_MODULE=gs3.setting

ENV REDIS_URL=redis://redis-18739.c212.ap-south-1-1.ec2.cloud.redislabs.com:18739/

EXPOSE 80

# CMD   daphne -b 127.0.0.1 -p 8000 gs3.asgi:ch
CMD  uvicorn gs3.asgi:application --host 0.0.0.0 --port 80 --reload

