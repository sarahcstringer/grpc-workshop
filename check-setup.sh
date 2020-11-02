#!/bin/bash

source venv/bin/activate
python3 00-test-setup/server.py & PROC_ID=$!
echo $(python3 00-test-setup/client.py)
kill "$PROC_ID" 
