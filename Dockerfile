FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
WORKDIR /usr/src/app

RUN apt --yes install git bash
RUN git clone https://github.com/NxPKG/binance-connector-python.git \
    && cd binance-connector-python \
    && python3 setup.py \
    && binance-connector-python -u force

CMD ["binance-connector-python"]
