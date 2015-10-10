#!/usr/bin/env bash

# Init.
apt-get update

# Install node.
NODE_VERSION=0.12.0
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

# Install rbenv and rubies.
su - vagrant -c <<SCRIPT
sudo apt-get -y purge ruby
sudo apt-get -y autoremove
sudo apt-get install -y libssl-dev zlib1g-dev libreadline-dev
if [ ! -d ~/.rbenv ]; then
  git clone git://github.com/sstephenson/rbenv.git ~/.rbenv
  git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
fi
echo 'export PATH="/home/vagrant/.rbenv/bin:$PATH"' > ~/.bash_profile
echo 'eval "$(rbenv init -)"' >> ~/.bash_profile
source ~/.bash_profile

[ -d ~/.rbenv/versions/2.2.2 ] || rbenv install 2.2.3
rbenv rehash
SCRIPT

# Install redis
add-apt-repository -y ppa:rwky/redis
apt-get update
apt-get install -yq redis-server

