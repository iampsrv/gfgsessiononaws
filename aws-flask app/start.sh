#!/bin/bash -ex

# Update system
apt update -y
apt upgrade -y

# Install dependencies
apt install -y python3 python3-pip python3-venv git

# Move to home directory
cd /home/ubuntu

# Clone the repo
git clone https://github.com/iampsrv/aws-flask.git
cd aws-flask

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install required packages
pip install --upgrade pip
pip install flask boto3

# Run the Flask app in background and log output
nohup venv/bin/python3 app.py > app.log 2>&1 &
