# Pull base image

FROM python:3.8

# Set environmental variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory

WORKDIR /code

# Install dependancies

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#Copy project 

COPY . /code/

