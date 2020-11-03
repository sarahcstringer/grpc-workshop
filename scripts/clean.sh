#!/bin/bash
echo "Removing python3 virtual environment"
rm -rf ./venv/
echo "Killing any running servers on port 50051"
lsof -nP -iTCP -sTCP:LISTEN | grep 50051 | cut -f2 -d " " | xargs kill
