FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apt-get update
RUN \
    apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt


# copy entrypoint.sh
COPY ../entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

RUN . ./entrypoint.sh
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app.main:app"]
# CMD ls -a
ENTRYPOINT . ./entrypoint.sh