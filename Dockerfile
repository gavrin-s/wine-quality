FROM python:3.7.1-stretch

LABEL maintainer="Sergey Gavrin <gavrin_sv@bw-sw.com>"

EXPOSE 9999

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV FILL=1

COPY . /
CMD ["gunicorn", "-b", "0.0.0.0:9999", "rest_api:app"]