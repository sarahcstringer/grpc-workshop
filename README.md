# Python gRPC Workshop

## Prerequisites

This workshop requires you to have python3 installed (>=3.6).

### Setup

1. Clone this repository and cd into the `grpc-workshop` directory: `git clone https://github.com/sarahcstringer/grpc-workshop.git && cd grpc-workshop`
2. Create a new python3 virtual environment: `python3 -m venv venv`
3. Source the new virtual environment: `source venv/bin/activate`
4. Install the required packages: `pip3 install -r requirements.txt`

### Test that the environment is set up correctly

`00-test-setup` contains a small gRPC client and server that you can run to verify you have gRPC correctly installed.

1. `cd 00-test-setup` and run `python3 server.py` to run the gRPC server.
2. Open a second tab, and run `python3 client.py` from the `00-test-setup` folder as well. After running the client, you should see the output "Setup successful!".
Then you can quit the server that's running in the other tab (with control-c).

## Workshop

### Additional Exercises

There are several other exercises in the `additional-exercises` folder for more practice with various aspects of gRPC.
