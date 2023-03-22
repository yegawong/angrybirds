# The base-deps Docker image installs main libraries needed to run Angrybirds

FROM ubuntu:latest
ADD ssl.tar /usr/local

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y \
        net-tools \
        iputils-ping \
        qt5-default \
        python3.6 \
        python3-pip \
    && pip3 install psutil==5.7.0 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install gym==0.16.0 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install ray==0.8.5 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install torch==1.3.1 torchvision==0.4.2 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install tensorflow==1.14.0 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install Twisted==19.10.0 -i https://mirrors.aliyun.com/pypi/simple/ \
    && apt-get clean \
    && rm -rf /root/.cache/pip/ \
    && rm -f /usr/bin/openssl \
    && ln -s /usr/local/ssl/bin/openssl /usr/bin/openssl \
    && echo 'ulimit -c 0' >> /etc/profile
# For Click
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8