FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN mkdir /static
WORKDIR /code

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD django-app /code
ADD secretkey.txt /

CMD python3 manage.py collectstatic --noinput && gunicorn mysite.wsgi -b 0.0.0.0:80
