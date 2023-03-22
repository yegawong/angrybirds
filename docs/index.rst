.. Stockman documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:00:00 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Getting Started with Angrybirds
==============================
``angrybirds`` makes no assumptions about the structure of your agent, 
and is compatible with any numerical computation library, such as TensorFlow 
or Theano. You can use it from Python code, and soon from other languages.

Quick start
^^^^^^^^^^^
Supported systems
-----------------
We currently support Windows running Python 3.4 -- 3.7. 


Assuming you have Python already, install Angrybirds:

.. code:: shell

    git clone https://fit.domocloud.cn:8888/birdbreeding/angrybirds.git
    cd <Folder>
    pip install -U . or pip install -e .

Testing
-------

.. code:: shell

    python3 test_env.py


Guide
^^^^^

.. code:: python

    import angrybirds

    env = gym.make(register_id)  """创建相应环境"""
    env.action_space             """ 环境的动作空间 """
    env.observation_space        """ 环境的状态空间 """

    env.reset(self)              """重置环境"""

    env.step(self, action)       """action: list""

    env.close(self)              """关闭环境，主动调用"""

.. toctree::
   :maxdepth: 4
   :caption: Contents:
   
   indices
   license
   help

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
