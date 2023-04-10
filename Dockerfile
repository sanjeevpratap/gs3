FROM python:3.10-slim-buster

ENV PYTHONBUFFERED=1

RUN mkdir /app1

WORKDIR /app1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000

