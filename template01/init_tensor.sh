#!/bin/bash
export TF_VER=0.12.1
export TF_PY_VER=35
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TF_VER}-cp${TF_PY_VER}-cp${TF_PY_VER}m-linux_x86_64.whl
export TF_BIN_DIR=env/tensorflow

# set up the virtual env.
#pip3 install virutalenv
#pyenv env # --system-site-package ${TF_VIRTUAL_ENV_DIR}
python3 -m venv ${TF_BIN_DIR}

# tensor env.
source env/bin/activate  # If using bash

# isntall tensorflow
pip3 install --upgrade $TF_BINARY_URL

# upgrade pip in virtualenv
pip3 install --upgrade pip