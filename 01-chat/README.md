# Chat Application Workshop

## Existing application

The existing application is a chat app that allows clients to send messages to a general chat room.

### Running the application

- Activate your virtualenv: `source ../venv/bin/activate`
- Run `server.py`: `python3 server.py`. This will display a message that the server is running, and then the process will hang, waiting for requests from clients.
- Open a separate tab, and run a client: `python3 client.py`. The client will display a startup message, and then hang, waiting for a user to type a message. Here, you can type and see the message get sent.
- To see that the messages get streamed to all clients, open another tab and start a new client (there should be 2 clients running now): `python3 client.py`. Send a message in one client, and see it appear in the other client screen.

### Code Walkthrough

The following files are already defined:

1. `chat.proto`: A protocol buffer file that contains the service definition for this app.
2. `chat_pb2.py`: The auto-generated Python message types.
3. `chat_pb2_grpc.py`: The auto-generated Python client and server stubs.
4. `server.py`: Logic for the chat server.
5. `client.py`: Logic for a python client to interact with the server.

## Your Task

Right now, there's no way to tell who sent which message in the chat.
Your task it to add the notion of a User to this service, and keep track of which user
sends a particular message. When displaying messages, display the username of the
user who sent the message in front of the text of their message. Example:

```
alice: hi, this is alice
bob: hi, it's bob
```

Additionally, it would be helpful for the server to keep track of usernames so only unique usernames
can be used. If someone signs up with a username that's already used, the server should return a message
that the username is taken, and the client should prompt for a new username from the user.

### General Steps

To accomplish this, you'll need to update a few different pieces of code:

#### Updates to `chat.proto`

The service definition will need a few updates:
- A new User type
- Messages will need to be updated to add which User sent the message
- There will need to be a new AddUser RPC

#### Re-compile the protobuf file, re-generate Python code stubs

Once updating `chat.proto`, you'll need to re-compile the protobufs and re-generate the Python code stubs:

```
python3 -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. chat.proto

# Arguments used:
# -I: the proto path. Where to find the specified proto input file.
# --python_out: Generate a Python source file with message/service definitions in the given directory.
# --grpc_python_out: Generate a Python source file with client/server bindings in the given directory.
# chat.proto: The input .proto file.
# For more help: python3 -m grpc_tools.protoc -h
```

#### Updating client and server logic

The client and server will now need to be updated with the new service definitions.

The server will have to be updated to accept a request to add a new user, and keep track of unique usernames.

The client will need to ask the user for a username when starting up (you can use Python's `input()` function to prompt the user for input from the command line). It will then need to send a request to the server to add that new user, and keep prompting if the user did not enter a unique username. The client will also need to send along the username with every message that the user sends to the server. Additionally, the client will need to be updated to print a username along with printing each message that is streamed from the server.

### Example solution

There are many ways to approach this feature. One possible solution is in [`solutions/01-add-user`](https://github.com/sarahcstringer/grpc-workshop/tree/master/01-chat/solutions/01-add-user).


## Stretch goal

Once you've implemented the feature above, try to implement a direct message feature.

If a user sends a message that begins with `@<existing username>`, send that message to *only that user*. No one else in the chat should receive that particular message. 

### Hints

For this feature, you'll need to keep track of which user is interacting from which client. A helpful object
here is the `context` that is passed in to every request, from the client to server.

For example:

```
def SendMessage(self, request, context):
    ...
```

This `context` object contains information about the `peer`, or the client that sent the request. You can use `context.peer()` to
get a unique address for that client, and store that information along with the username.

### Example solution

As with the first feature, there are many ways to approach this feature. One possible solution is in [`solutions/02-direct-message`](https://github.com/sarahcstringer/grpc-workshop/tree/master/01-chat/solutions/02-direct-message).

## Futher improvements: Enums and status codes

One further improvement that could be made to the `AddUser` feature would be a specific list of status codes that can be sent back from a server, depending on whether a username is taken or not. This way, the client does not need to check for a specific string, and can rely on a stable, codified Status Code object.

Check out [`Enumerations`](https://developers.google.com/protocol-buffers/docs/proto#enum) in protocol buffers, and add an `enum` for Status Code. This way, when a client sends a request to add a user, the server will send back either a code for ADDED or a code for NOT_ADDED.

### Example solution

Take a look at [`solutions/03-status-code`](https://github.com/sarahcstringer/grpc-workshop/tree/master/01-chat/solutions/03-status-code) for one potential solution.

