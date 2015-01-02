#!/usr/bin/env bash

# Init.
apt-get update

# Install node.
NODE_VERSION=0.10.32
apt-get -y install g++ gcc make
wget http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz -O /tmp/nodejs.tar.gz
tar -xzvf /tmp/nodejs.tar.gz -C /home/vagrant
chown -R vagrant:vagrant /home/vagrant/node-v$NODE_VERSION
su - vagrant -c "/home/vagrant/node-v$NODE_VERSION/configure"
su - vagrant -c "cd /home/vagrant/node-v$NODE_VERSION; make"
su - vagrant -c "cd /home/vagrant/node-v$NODE_VERSION; sudo make install"

# Install dependencies.
apt-get install -y git-core

# Install D programming language.
apt-get install -y gdc

# Setup the python virtualenv.
sudo apt-get install -y python-pip python-dev
sudo pip install virtualenv
sudo pip install virtualenvwrapper
