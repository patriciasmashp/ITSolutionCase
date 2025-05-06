# pull official base image
FROM python:3.10-alpine

# set work directory
ADD . /app
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000

