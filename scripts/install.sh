#!/bin/bash
MINOR_VERSION=$(python3 --version | cut -f2 -d' ' | cut -d. -f2 )
if [ "$MINOR_VERSION" -lt 7 ]
then
    echo "Python3 version needs to be 3.7 or higher."
    exit 1
fi
echo "Creating a python 3 virtual environment."
python3 -m venv venv
source venv/bin/activate
echo "Installing requirements in virtual environment."
pip install --upgrade pip && pip install -r requirements.txt
echo "Setup complete."
