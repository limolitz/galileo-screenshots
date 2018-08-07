FROM python:3.6
RUN apt-get update && apt-get install -y --no-install-recommends rabbitmq-server apt-transport-https ca-certificates curl gnupg && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && apt-get update && apt-get install -y --no-install-recommends google-chrome-stable

RUN pip install pipenv

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD Pipfile /code/
ADD Pipfile.lock /code/
RUN pipenv install --system
ADD . /code/

CMD ./starter.sh
