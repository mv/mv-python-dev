#!/bin/bash
#
# Provision Python Pyenv for Linux
#

export HOME=/home/vagrant
export bashrc=${HOME}/.bashrc

## Add first so I can bypass install warning
if ! grep -q pyenv ${bashrc}
then
  echo '' >> ${bashrc}
  echo 'export PATH="/home/vagrant/.pyenv/bin:$PATH"' >> ${bashrc}
  echo 'eval "$(pyenv init -)"'                       >> ${bashrc}
  echo 'eval "$(pyenv virtualenv-init -)"'            >> ${bashrc}
  echo '' >> ${bashrc}
  source ${bashrc} 2>/dev/null
fi


## Fix install if provision is by root user
export PYENV_ROOT=${HOME}/.pyenv

if [ ! -d ${PYENV_ROOT} ]
then
  curl -s https://pyenv.run | bash
  chown -R vagrant:vagrant ${PYENV_ROOT}
fi

## Add dependencies for compiling/installing Python
sudo yum install -y openssl-devel bzip2-devel libffi-devel
sudo yum install -y readline-devel sqlite-devel expat-devel
