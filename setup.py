import sys
import os.path
from setuptools import setup, find_packages

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'angrybirds'))

# Environment-specific dependencies.
with open('requirements.txt') as f:
    install_requires = f.readlines()

CURRENT_PYTHON = sys.version_info[:2]
MIN_PYTHON = (3, 4)

if CURRENT_PYTHON < MIN_PYTHON:
    sys.stderr.write("""
        ============================
        Unsupported Python Version
        ============================

        Python {}.{} is unsupported. Please use a version newer than Python {}.{}.
    """.format(*CURRENT_PYTHON, *MIN_PYTHON))
    sys.exit(1)

with open('VERSION') as f:
    VERSION = f.read().strip()

setup(
    name='angrybirds',
    version=VERSION,
    description='angrybirds: A toolkit for developing and quick train your reinforcement learning agents.',
    url='https://fit.domocloud.cn:8888/birdbreeding/angrybirds.git',
    author='alan.dev',
    author_email='alan@alan',  # @TODO this might need refinement
    license='',
    packages=[package for package in find_packages() if package.startswith('angrybirds')],
    zip_safe=False,
    install_requires=install_requires,
    tests_require=['pytest', 'mock'],
    python_requires='>=3.4',
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
