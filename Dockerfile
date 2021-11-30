FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1


RUN apt-get update

RUN apt-get install -y gnuplot


WORKDIR /app

ADD . /app


RUN pip install --upgrade pip

RUN pip install pip install -r requirements.txt


RUN chmod +x gunicorn_start.sh


EXPOSE 5000

CMD ["./gunicorn_start.sh"]