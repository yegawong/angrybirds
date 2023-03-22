# The base-deps Docker image installs main libraries needed to run Angrybirds
# # Add the package repositories
# $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
# $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
# $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# $ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
# $ sudo systemctl restart docker

FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y \
        python3.6 \
        python3-pip \
    && pip3 install torch==1.3.1 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install gym==0.16.0 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install psutil==5.7.0 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install ray==0.8.5 -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip3 install setproctitle==1.1.10 -i https://mirrors.aliyun.com/pypi/simple/ \
# For Click
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8