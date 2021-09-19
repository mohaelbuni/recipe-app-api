FROM python:3.9.0a5-alpine3.10


ENV PYTHONUNBUFFERED 1
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt


RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user




# FROM python:alpine3.10
# LABEL AUTHOR="mohaelbuni"

# ENV PYTHONUNBUFFERED 1

# RUN /usr/local/bin/python -m pip install --upgrade pip

# COPY ./requirements.txt /requirements.txt
# RUN pip install -r /requirements.txt

# RUN mkdir /app
# WORKDIR /app
# COPY ./app /app

# RUN adduser -D user
# USER user
