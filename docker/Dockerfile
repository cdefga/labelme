FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq && \
    apt-get install -qq -y \
    git \
    python3 \
    python3-pip \
    python3-matplotlib \
    python3-pyqt5 \
    openjdk-11-jdk \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -U pip setuptools wheel

RUN mkdir labelme
WORKDIR /root/labelme
COPY . .
RUN chmod u+rx script.sh
RUN python3 -m pip install .

RUN mkdir /root/workdir
ENV LANG en-US
WORKDIR /root/workdir

ENTRYPOINT ["python3", "-m", "labelme"]
