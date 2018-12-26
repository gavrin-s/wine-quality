FROM python:3.7.1-stretch

LABEL maintainer="Sergey Gavrin <gavrin_sv@bw-sw.com>"

RUN mkdir /ds

EXPOSE 5000

ADD model /ds/model
ADD scaler /ds/scaler
ADD rest_api.py /ds/rest_api.py
ADD winequality-white.csv /ds/winequality-white.csv
ADD ./requirements.txt /

RUN pip3 install -r requirements.txt

ADD start.sh /ds/start.sh

WORKDIR /ds
ENTRYPOINT ["bash", "start.sh"]