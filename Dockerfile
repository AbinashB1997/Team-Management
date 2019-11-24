FROM python:3

ADD . /app
WORKDIR /app

RUN pip3 install flask
RUN pip3 install pymongo

EXPOSE 5000

CMD ["python3", "app.py"]