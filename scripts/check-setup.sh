#!/bin/bash

source venv/bin/activate
python3 00-test-setup/server.py & SERVER_PROC_ID=$!
SECONDS=0
while ! (lsof -Pi :50051 -sTCP:LISTEN -t >/dev/null)  && [[ "$SECONDS" -lt 10 ]]  ; do
    sleep 1
done

if [ $SECONDS -gt 9 ]
then
    echo "gRPC server did not start within 10 seconds"
    exit 1
fi

python3 00-test-setup/client.py & CLIENT_PROC_ID=$!
wait $CLIENT_PROC_ID
kill "$SERVER_PROC_ID"
