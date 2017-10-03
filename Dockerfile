FROM python:3

RUN mkdir /code
WORKDIR /code

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD django-app /code
ADD secretkey.txt /

CMD ["/code/manage.py", "runserver", "0.0.0.0:80"]
ENTRYPOINT ["python3"]
