#!/bin/bash
sudo apt update
sudo apt-get install python3-venv -y


# Test Phase
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt


# pytest goes here


# Deploy Phase


# Make the installation directory
sudo mkdir /opt/<todo-list-app>


# Give jenkins user permissions for the installation directory
sudo chown -R jenkins /opt/<todo-list-app>


sudo systemctl daemon-reload
sudo systemctl stop <todo-list-app.service > file
sudo systemctl start <todo-list-app.service> file
