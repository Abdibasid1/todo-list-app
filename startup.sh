a!/bin/bash
cd /opt/todo-list-app
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirement.txt
python3 app.py
