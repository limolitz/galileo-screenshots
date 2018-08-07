FROM python:3.6
RUN apt-get update && apt-get install -y --no-install-recommends rabbitmq-server
RUN pip install pipenv

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD Pipfile /code/
ADD Pipfile.lock /code/
RUN pipenv install --system
ADD . /code/

CMD ./starter.sh
