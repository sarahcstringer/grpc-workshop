import threading

import chat_pb2
import chat_pb2_grpc
import grpc


class ChatClient(object):
    def __init__(self, host="localhost", port="50051"):
        self.host = host
        self.port = port
        # Creates an insecure channel to a server
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        # This stub can be used to invoke methods on the server
        self.stub = chat_pb2_grpc.ChatStub(self.channel)

    def send_message(self, msg):
        self.stub.SendMessage(chat_pb2.Message(msg=msg))

    def start_listening_thread(self):
        """Begin a background thread to listen for streamed messages from the server."""

        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        """Listen for and print messages streamed from the server."""
        for msg in self.stub.Listen(chat_pb2.ListenRequest()):
            print(f">>> {msg.msg}")


def main():
    client = ChatClient()
    client.start_listening_thread()
    print("client initiated. Start chatting by typing anything and pressing enter.")
    # wait in a loop for user input, and send messages when input is entered
    while True:
        message = input()
        client.send_message(message)


if __name__ == "__main__":
    main()
