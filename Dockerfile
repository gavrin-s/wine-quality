FROM ubuntu:16.04

LABEL maintainer="Sergey Gavrin <gavrin_sv@bw-sw.com>"

RUN apt-get update \
    && apt-get -y install python3 \
    python3-pip

RUN mkdir ds
ENV HOME=/ds
ENV SHELL=/bin/bash

VOLUME /ds
WORKDIR /ds

ADD model /ds/model
ADD rest_api.py /ds/rest_api.py
ADD requirements.txt /ds/requirements.txt

RUN pip3 install -r requirements.txt

ADD rest_api.py /ds/rest_api.py

RUN python3 rest_api.py

ADD run_jupyter.sh /ds/run_jupyter.sh

RUN ["/bin/bash"]
