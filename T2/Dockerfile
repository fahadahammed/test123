FROM ubuntu:20.04

MAINTAINER Fahad Ahammed - email: iamfahadahammed@gmail.com

WORKDIR /opt/

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip
COPY . .

RUN pip3 install --no-cache-dir flask

EXPOSE 5100

CMD ["python3", "app.py"]