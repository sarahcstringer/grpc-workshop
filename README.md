# Python gRPC Workshop

## Prerequisites

This workshop requires you to have Python 3 installed (>=3.7).

You can check your Python version with `python3 --version`. If it is lower than Python 3.7, you'll need to update the version for this workshop. (Note: [`pyenv`](https://github.com/pyenv/pyenv) is a great tool for managing multiple Python versions on a machine.)

### Setup

1. Clone this repository and cd into the `grpc-workshop` directory: `git clone https://github.com/sarahcstringer/grpc-workshop.git && cd grpc-workshop`
2. Create a new Python 3 virtual environment: `python3 -m venv venv`
3. Source the new virtual environment: `source venv/bin/activate`
4. Install the required packages: `pip3 install -r requirements.txt`

### Test that the environment is set up correctly

The [`00-test-setup` folder](https://github.com/sarahcstringer/grpc-workshop/tree/master/00-test-setup) contains a small gRPC client and server that will be used to test your setup. To verify that your setup is working, run the `check-setup.sh` script. It will source your virtual environment (which should be named `venv`), start up the test server, and run the client to make a request to the server. You should see the following output when you run the script:

```
$ bash check-setup.sh
gRPC server is running.
Received request from gRPC client.
Setup successful!
```

### Troubleshooting

Potential issues that might occur with setup:

#### Virtual environment not named venv

If you see the following output, either rename your virtual environment to "venv" (following the instructions above), or update the `check-setup.sh` script to refer to the name of your virtual environment.

```
check-setup.sh: line 3: venv/bin/activate: No such file or directory
```

#### grpc module not found

If you see the following output, verify that you have a virtual environment and that it contains `grpcio` (`pip3 freeze | grep grpc`). If you don't have `grpcio`, re-install the requirements.

```
Traceback (most recent call last):
    File "00-test-setup/server.py", line 3, in <module>
        import grpc
ModuleNotFoundError: No module named 'grpc'
```

#### Server not starting up

If you see the following output, verify that no processes are running on port 50051 on your local machine. Try running the gRPC server directly, by running `python3 00-test-setup.py` and see if additional errors occur.

```
gRPC server did not start within 10 seconds
```

## Workshop

## Additional Exercises

For more practice with gRPC concepts, check out the [`additional-exercises`](https://github.com/sarahcstringer/grpc-workshop/tree/master/additional-exercises) folder.
