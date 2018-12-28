FROM python:3.7.1-stretch

LABEL maintainer="Sergey Gavrin <gavrin_sv@bw-sw.com>"

RUN mkdir /ds

EXPOSE 9999

COPY requirements.txt .
RUN pip3 install -r requirements.txt

# лишний раз скопируем requirements.txt, ну и ладно
COPY . /ds
WORKDIR /ds


ENTRYPOINT ["python3", "rest_api.py"]