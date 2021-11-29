FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

RUN chmod +x gunicorn_start.sh

CMD ["./gunicorn_start.sh"]