Galileo Screenshots
===================

A tool which allows user to screenshot any website. It is written in Django and offers a web frontend and a backend, which does the actual screenshotting. Between the frontend and the backend, message queues are used for communication.

Install
=======
* Install pipenv
* Install Python virtualenv with pipenv

```bash
 pipenv install
```


Run
===
Only the built-in development server of Django is supported so far.
```bash
pipenv shell
python3 manage.py runserver
```
