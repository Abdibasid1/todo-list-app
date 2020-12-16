#!/bin/bash
sudo apt update
sudo apt-get install python3-venv -y
 
# Test Phase
cd $WORKSPACE
ls -lah
sudo cp -r $WORKSPACE /opt/jenkins
sudo chown -R jenkins /opt/jenkins
 
cd /opt/jenkins
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
python setup.py bdist_wheel 
pip3 install -r requirement.txt
cat requirement.txt
 
# pytest goes here
 
# Deploy Phase

sudo systemctl daemon-reload
sudo systemctl stop todo-list-app.service
sudo systemctl start todo-list-app.service
 
