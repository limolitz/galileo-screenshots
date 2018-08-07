Galileo Screenshots
===================

A tool which allows user to screenshot any website. It is written in Django and offers a web frontend and a backend, which does the actual screenshotting. Between the frontend and the backend, message queues are used for communication.

Install
=======
* Install pipenv, RabbitMQ
* Put a chromedriver in your $PATH
* Install Python virtualenv with pipenv

```bash
 pipenv install
```


Run
===
Only the built-in development server of Django is supported so far.
```bash
pipenv shell
python3 manage.py migrate
python3 manage.py runserver
```

Celery is used for the backend which needs to be run as well. In a development environment, you can start it by calling
```bash
pipenv shell
celery -A galileo_screenshots worker -l info
```


References
==========
I used several tutorials for bootstrapping this project:
* https://djangoforbeginners.com/message-board/
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views
* https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html
