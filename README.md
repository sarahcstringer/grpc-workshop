# Python gRPC Workshop

## Prerequisites

This workshop requires you to have Python 3 installed (>=3.7).

You can check your Python version with `python3 --version`. If it is lower than Python 3.7, you'll need to update the version for this workshop. (Note: [`pyenv`](https://github.com/pyenv/pyenv) is a great tool for managing multiple Python versions on a machine.)

### Setup

- Clone this repository and cd into the `grpc-workshop` directory: `git clone https://github.com/sarahcstringer/grpc-workshop.git && cd grpc-workshop`
- Run `make setup` to run the setup for this workshop. The script will:
    - Check your python 3 version
    - Create a new virtual environment named `venv`
    - Source the virtual environment and install required packages
    - Run the test gRPC client and server in `00-test-setup` to verify installation
    - The last output of the script should say `Setup successful!`

## Slides

To view slides, open `slides/index.html`.

## Workshop

## Additional Exercises

For more practice with gRPC concepts, check out the [`additional-exercises`](https://github.com/sarahcstringer/grpc-workshop/tree/master/additional-exercises) folder.
