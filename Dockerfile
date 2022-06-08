FROM ubuntu:focal
ARG CLICK_VERSION

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \
    && apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        gnupg \
        python3-distutils \
        software-properties-common \
        wget

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN wget -q https://bootstrap.pypa.io/get-pip.py \
       && python3 get-pip.py pip==21.3.1 \
       && rm get-pip.py

RUN pip install click==$CLICK_VERSION pytest==7.1.2

COPY ./ code/
