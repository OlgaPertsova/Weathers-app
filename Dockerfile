FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD . /code/
ADD .env.docker /code/.env

ENV APP_NAME=DOCKER_WEATHERS_APP

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8001