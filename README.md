# Python gRPC Workshop

## Prerequisites

This workshop requires you to have python3 installed (>=3.7).

### Setup

1. Clone this repository and cd into the `grpc-workshop` directory: `git clone https://github.com/sarahcstringer/grpc-workshop.git && cd grpc-workshop`
2. Create a new python3 virtual environment: `python3 -m venv venv`
3. Source the new virtual environment: `source venv/bin/activate`
4. Install the required packages: `pip3 install -r requirements.txt`

### Test that the environment is set up correctly

The [`00-test-setup` folder](https://github.com/sarahcstringer/grpc-workshop/tree/master/00-test-setup) contains a small gRPC client and server that will be used to test your setup. To verify that your setup is working, run the `check-setup.sh` script. It will source your virtual environment (named `venv`), start up the test server, and run the client to make a request to the server. You should see the following output when you run the script:

```
$ bash check-setup.sh
gRPC server is running.
Received request from gRPC client.
Setup successful!
```

## Workshop

## Additional Exercises (work in progress)

For more practice with gRPC concepts, check out the [`additional-exercises`](https://github.com/sarahcstringer/grpc-workshop/tree/master/additional-exercises) folder.
