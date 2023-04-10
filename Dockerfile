FROM python:3.10-slim-buster

ENV PYTHONBUFFERED=1

RUN mkdir /app1

WORKDIR /app1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 6379

CMD python manage.py runserver 0.0.0.0:8000

