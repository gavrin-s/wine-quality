FROM python:3.7.1-stretch

LABEL maintainer="Sergey Gavrin <gavrin_sv@bw-sw.com>"

RUN mkdir /ds

EXPOSE 9999

COPY model /ds/model
COPY scaler /ds/scaler
COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY rest_api.py /ds/rest_api.py

WORKDIR /ds
CMD ["python3", "rest_api.py"]