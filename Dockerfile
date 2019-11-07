FROM ubuntu:latest
LABEL naifmhd "naifmhd@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y python-pip python-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python python \
    && pip install --upgrade pip

RUN apt-get update \
    && apt-get install -y python-tk ffmpeg portaudio19-dev python-pyaudio

COPY requirements.txt /

RUN pip install -r /requirements.txt

# COPY src/ /app

# COPY mp3/ /app/mp3

WORKDIR /

# ENTRYPOINT ["/bin/sh"]