FROM python:3.7.4

MAINTAINER Lutaaya Huzaifah Idris

ADD . /app

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

# Run run.py when the container launches
COPY run.py /app
CMD python3 run.py

