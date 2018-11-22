#!/bin/bash
# to abort if any process return a non-zero value
set -e

cd ~
echo "[1] I am in `pwd`..."
echo "[2] Upgrading the repos..."
apt-get upgrade -y
wait

mkdir "Downloads"
echo "[3] Starting the install of docker..."
echo "[3] Installing some docker packages..."
apt-get install apt-transport-https ca-certificates curl software-properties-common -y
wait

echo "[3] Adding docker's official GPG key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
wait

echo "[3] Setting up stable repo for docker..."
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
wait

echo "[3] Installing docker..."
apt-get update
wait
apt-get install docker-ce -y
wait

echo "[3] Docker succesfully installed..."
echo "[4] Installing Anaconda in silent mode..."
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh -O ~/anaconda.sh
wait
bash ~/anaconda.sh -b -p $HOME/anaconda3
wait
export PATH="$HOME/anaconda3/bin:$PATH"
wait
echo "PATH=$HOME/anaconda3/bin:$PATH" >> ~/.bashrc
wait
echo "[4] Anaconda successfully installed..."
echo "[5] Tidying up..." rm ~/anaconda.sh
echo "[6] Setting up git..."
wait
mkdir $HOME/git
wait
echo "[7] adding the user to docker group"
usermod -a -G docker $USER
usermod -aG sudo $USER

exit $?
