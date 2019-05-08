FROM ubuntu:18.04

ENV PYTHON_VERSION=3.7.2
ENV PYENV_VERSION=1.2.11

ENV DEBIAN_FRONTEND=noninteractive

USER root
RUN apt update -y && apt upgrade -y && apt install -y git make build-essential \
sudo bash zsh curl wget nano vim tmux htop tzdata locales \
postgresql-client iputils-ping telnet \
libev-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils \
tk-dev libffi-dev liblzma-dev python-openssl \
mysql-client libmysqlclient-dev \
libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
&& apt clean \
&& rm -rfv /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV USER=web-user
ENV HOME=/home/$USER

ENV APP_NAME=python_app
ENV APP_DIR=/$APP_NAME

ENV PYENV_DIR=$HOME/.pyenv
ENV PYENV_BIN_ROOT=$PYENV_DIR/bin
ENV PYENV_BIN=$PYENV_BIN_ROOT/pyenv
ENV ENV_BIN_ROOT=$PYENV_DIR/versions/$APP_NAME/bin
ENV ENV_PYTHON_BIN=$ENV_BIN_ROOT/python
ENV ENV_PIP_BIN=$ENV_BIN_ROOT/pip

ARG DEV_DIR=dev

ENV SHELL_FN=.shell_pyenv
ENV SHELL_ENV_FP=$HOME/$SHELL_FN

USER root
RUN useradd -m -s /bin/bash -u 5000 -U $USER # important on linux platform, you need to create user for docker with same uid (5000)
RUN echo 'Europe/Kiev' > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

USER $USER
WORKDIR $HOME
RUN git clone https://github.com/pyenv/pyenv.git $PYENV_DIR \
&& git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_DIR/plugins/pyenv-virtualenv \
&& cd $PYENV_DIR && git checkout tags/v$PYENV_VERSION

WORKDIR $HOME
COPY $DEV_DIR/$SHELL_FN $HOME
USER root
RUN chown $USER:$USER $HOME/$SHELL_FN
USER $USER
RUN echo ". $SHELL_ENV_FP" >> $HOME/.bashrc

RUN $PYENV_BIN install $PYTHON_VERSION \
&& $PYENV_BIN virtualenv $PYTHON_VERSION $APP_NAME

USER root
RUN mkdir $APP_DIR && chown $USER:$USER -R $APP_DIR

# ohmyzsh
ENV ZSH_CONF_FN=.zshrc
ENV ZSH_CONF_FP=$HOME/$ZSH_CONF_FN
USER root
RUN chsh $USER -s /bin/zsh

# Set the locale
USER root
ARG LANG=en_US.UTF-8
RUN locale-gen $LANG
ENV LANG=$LANG
ENV LANGUAGE=en_US:en
ENV LC_ALL=$LANG

ENV TERM=xterm
USER $USER
WORKDIR $HOME
# run the installation script
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true \
&& echo ". $SHELL_ENV_FP" >> $ZSH_CONF_FP \
&& sed -i -e 's/plugins=(git)/plugins=(git python django docker nmap pip postgres rsync sudo tmux systemd)/g' $ZSH_CONF_FP \
&& sed -i -e 's/ZSH_THEME="robbyrussell"/ZSH_THEME="ys"/g' $ZSH_CONF_FP \
&& echo "export LANG=$LANG" >> $ZSH_CONF_FP \
&& echo "workon $APP_NAME" >> $ZSH_CONF_FP
