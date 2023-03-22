**Status:** Maintenance (expect bug fixes and minor updates)

Angrybirds
**********

**Angrybirds is a toolkit for developing and comparing reinforcement learning algorithms.** This is the ``angrybirds`` open-source library, which gives you access to a standardized set of environments.It need the action of red planes and fixed rules to fight against opponents. env return to the status of the two planes in the simulation.

`See What's New section below <#what-s-new>`_

``angrybirds`` makes no assumptions about the structure of your agent, and is compatible with any numerical computation library, such as TensorFlow or Theano. You can use it from Python code, and soon from other languages.

If you're not sure where to start, we recommend beginning with the
`docs <docs/build/index.html>`_ on our site. But html file is not exist, you need execute `'sphinx-apidoc -o ./full ../angrybirds/'` and `'sphinx-build.exe -b html ./ ./build/'`

**@Copyright OpenAI Gym**
A whitepaper for OpenAI Gym is available at http://arxiv.org/abs/1606.01540, and here's a BibTeX entry that you can use to cite it in a publication::

  @misc{1606.01540,
    Author = {Greg Brockman and Vicki Cheung and Ludwig Pettersson and Jonas Schneider and John Schulman and Jie Tang and Wojciech Zaremba},
    Title = {OpenAI Gym},
    Year = {2016},
    Eprint = {arXiv:1606.01540},
  }

.. contents:: **Contents of this document**
   :depth: 2

Basics
======

There are two basic concepts in reinforcement learning: the
environment (namely, the outside world) and the agent (namely, the
algorithm you are writing). The agent sends `actions` to the
environment, and the environment replies with `observations` and
`rewards` (that is, a score).

The core `angrybirds` interface is `Env <https://fit.domocloud.cn:8888/birdbreeding/angrybirds/blob/master/angrybirds/envs/slingshot.py>`_, which is
the unified environment interface. There is no interface for agents;
that part is left to you. The following are the ``Env`` methods you
should know:

- `reset(self)`: Reset the environment's state. Returns `observation`, `reward`, `done`, `info:{'crash':bool}`.
- `step(self, action)`: Step the environment by one timestep. Returns `observation`, `reward`, `done`, `info`.
- `render(self, mode='human')`: Render one frame of the environment. The default mode will do something human friendly, such as pop up a window. 

Supported systems
-----------------

We currently support Windows running Python 3.4 -- 3.7. 

Installation
============

You can perform a minimal install of ``angrybirds`` with:

.. code:: shell

    'download plugin_exe.tar.gz to $HOME'
    echo $HOME
    tar -zxvf <floder>/patch_for_plugin_exe_20191209.tar.gz $HOME
    qmake -v  'we use qt5, if not apt install qt5-default'
    openssl version 'version must be v1.0.2o, if not download openssl-1.0.2o.tar.gz, address is https://www.openssl.org/source/old/1.0.2/openssl-1.0.2o.tar.gz or nextcloud find it'
    'if your openssl version is 1.0.2o, please goto install angrybirds'
    tar -zxvf openssl-1.0.2o.tar.gz
    ./config
    make && make test 'Confirm that there are no error messages and have PASS printed words'
    make install
    which openssl  'example: /usr/bin/openssl'
    cp /usr/bin/openssl /usr/bin/openssl.old
    rm /usr/bin/openssl => 'Y'
    ln -s /usr/local/ssl/bin/openssl /usr/bin/openssl 'if /usr/bin/openssl is your used'
    ping fit.domocloud.cn   'auth server'
    git clone https://fit.domocloud.cn:8888/birdbreeding/angrybirds.git
    cd <floder>
    pip install -U . or pip install -e .


Examples
========

See the ``examples`` directory.

Testing
=======

We are using `pytest <http://doc.pytest.org>`_ for tests. You can run them via:

.. code:: shell

    python3 test_env.py

Docker environment
==================

- 仓库名称: thufit
- 仓库地域: 华北5（呼和浩特）
- 公网地址: registry.cn-huhehaote.aliyuncs.com/angrybirds/thufit
- 专有网络: registry-vpc.cn-huhehaote.aliyuncs.com/angrybirds/thufit

    .. code:: shell

        1. 登录阿里云Docker Registry
        $ sudo docker login --username=<username> registry.cn-huhehaote.aliyuncs.com
        用于登录的用户名为阿里云账号全名，密码为开通服务时设置的密码。


        2. 从Registry中拉取镜像
        $ sudo docker pull registry.cn-huhehaote.aliyuncs.com/angrybirds/thufit:[镜像版本号]

        3. 创建docker环境，保持后台运行
        $ sudo docker run -d <image name> /bin/bash -c "while true; do sleep 1;done"

        4. 进入容器
        $ sudo docker ps
        $ sudo docker exec -it <container_id> /bin/bash
        $ <ctrl>+<p>+<q> 退出容器保持后台运行,<ctrl>+<d> 直接退出容器，不后台运行
        $ sudo docker cp <src> <tag>   拷贝文件

- Docker — 从入门到实践 https://yeasy.gitbooks.io/docker_practice/

Extend
======

- 改变环境配置为plane_config.py文件,eg:EnvConfig.red_beat=1/EnvConfig.blue_beat=20 \\ env.reset()即环境交互拍数变为20拍
- 存储态势文件配置为plane_config.py文件,eg:EnvConfig.situation=1 \\ 需要重新make_env,态势文件目录plugin_exe/package/data
- 存储日志文件配置为plane_config.py文件,eg:EnvConfig.log_level=1 \\ 需要重新make_env,态势文件目录plugin_exe/package/log
- SelfplayEnv 自博环境,需要两机action
- BaselineEnv 可选参数:日志级别,选边,选择对手:'Nigel'不带电抗对手环境,'Mauro'带电抗对手环境
- plane_action.py和plane_situation.py为对象定义，数据整理Excel有相应含义介绍
- 使用手册下载地址: https://fit.domocloud.cn:8890/index.php/s/j9cb7MjMDXGHktg
- 仿真软件下载地址: https://fit.domocloud.cn:8890/index.php/s/AjRNeSBnW4moaCA
- 态势软件下载地址: https://fit.domocloud.cn:8890/index.php/s/EfbqETSC9wwAYpL
- 快仿更新日期(当前使用版本与本项目同步): 04/30/2020

Code style
==========

    See `Json of CodeStyle <docs/codestyle.md>`_.

Git
===

    See `Git Manage <docs/gitmanage.md>`_.


What's new
==========

- 2019-6-28 (v0.1.2)
    + 修复situation/action兼容快仿

- 2019-6-24 (v0.1.1)
    + 更新高保真接口,situation兼容快仿

- 2019-6-9 (v0.0.77)
    + update base depend dockerfile

- 2019-6-5 (v0.0.76)
    + delete all env
    + update SelfplayEnv & BaselineEnv
    + update test script

- 2019-5-9 (v0.0.74)
    + update plugin_exe 20200430
    + update plugin_exe validity of authentication 12/30/2020

- 2019-4-13 (v0.0.73)
    + k8s config yaml add eviction strategy

- 2019-3-30 (v0.0.72)
    + add select side, default is blue
    + env add select model, default is train

- 2019-3-24 (v0.0.7)
    + fixed first step observation confusion

- 2019-3-23 (v0.0.68)
    + add nigle_exam & mauro_exam env
    + update nigle_exam & mauro_exam env

- 2019-3-18 (v0.0.67)
    + add earlpig env
    + update baseline reset

- 2019-3-10 (v0.0.65)
    + update plane_config IEWS_HX/RADAR_HX range value

- 2019-2-29 (v0.0.64)
    + update plugin_exe 20200115
    + reslove nAlarmNum > 10 bug, nAlarmNum max value is 15.

- 2019-2-26 (v0.0.63)
    + update control action api of baseline env

- 2019-2-25 (v0.0.62)
    + update convert aidata & aiinputdata to baseline ctypes standard interface
    + update api generate_aiiputdata

- 2019-2-21 (v0.0.6)
    + update baseline of plugin_exe

- 2019-2-13 (v0.0.57)
    + update plugin_exe

- 2019-1-13 (v0.0.55)
    + update environmental services have been waiting to become timeouts
    + update environmental kill port create services connection plugin_exe
    + update environmental reset set action & plugin_exe lost connection

- 2019-1-15 (v0.0.54)
    + add plugin_exe api function
    + update env close bug

- 2019-1-6 (v0.0.50)
    + add cluster ray head public IP address
    + update Dockerfile
    + support docker kill process

- 2019-12-30 (v0.0.49)
    + fixed continuation reset env bug

- 2019-12-26 (v0.0.48)
    + update Dockerfile
    + fixed env close bug
    + add test plugin_exe step time python script
    + add cluster config
    + chang angrybrids to angrybirds, fixed error name
    + update auth server quit bug
    + update kubernets config
    + add kubernets ray test script

- 2019-12-25 (v0.0.43)
    + update authentication method, can train even if broken network
    + add Dockerfile

- 2019-12-9 (v0.0.4)
    + update authentication method, can train even if broken network

- 2019-12-9 (v0.0.3)
    + update environments
    + update readme

- 2019-11-29 (v0.0.21)
    + update readme
    + add error tips
    + update environment tools

- 2019-11-29 (v0.0.2)
    + update plugin_exe 11/28
    + add benchmark opponents

- 2019-11-22 (v0.0.1)
    + init angrybirds lib
