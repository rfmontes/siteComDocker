FROM python:3.7-slim

LABEL maintainer='Rafael Fernandes'

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
   apt-get install -y libjpeg-dev zlib1g-dev python3-dev build-essential

RUN mkdir /src
WORKDIR /src

ADD . .

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
