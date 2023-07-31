#!/bin/bash
sudo apt-get update
echo "\$nrconf{restart} = \"l\"" | sudo tee -a /etc/needrestart/needrestart.conf
sudo apt-get install -y python3-pip
sudo pip3 install scikit-learn==0.24.0
sudo pip3 install flask

