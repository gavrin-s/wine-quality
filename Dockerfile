FROM python:3.7.1-stretch

LABEL maintainer="Sergey Gavrin <gavrin_sv@bw-sw.com>"

RUN mkdir /ds

EXPOSE 5000

ADD model /ds/model
ADD scaler /ds/scaler
ADD rest_api.py /ds/rest_api.py
ADD ./requirements.txt /

RUN pip3 install -r requirements.txt

WORKDIR /ds
ENTRYPOINT ["python3", "rest_api.py"]