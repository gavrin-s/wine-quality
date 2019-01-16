FROM python:3.6.8-stretch

LABEL maintainer="Sergey Gavrin <gavrin_sv@bw-sw.com>"

EXPOSE 9999

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV FILL=1

WORKDIR /app
COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:9999", "rest_api:app"]