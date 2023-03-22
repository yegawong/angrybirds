# The base-deps Docker image installs main libraries needed to run Angrybirds

FROM angrybirds/base-deps-exe
ADD angrybirds.tar /work/angrybirds
RUN pip3 install /work/angrybirds -i https://mirrors.aliyun.com/pypi/simple/ \
    && rm -rf /root/.cache/pip/