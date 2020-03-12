FROM ubuntu:16.04

MAINTAINER Jan Tanja "tanjannibal@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app/

COPY ./docker/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt && \
    rm /app/requirements.txt

COPY ./src/ /app/src

ENTRYPOINT [ "python" ]

CMD [ "/app/src/main.py" ]