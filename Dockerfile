FROM python:latest

WORKDIR /usr/src

COPY application.py .

CMD [ "python", "application.py" ]