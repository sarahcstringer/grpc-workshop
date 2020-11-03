import threading

import chat_pb2
import chat_pb2_grpc
import grpc


class ChatClient(object):
    def __init__(self, host="localhost", port="50051"):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.stub = chat_pb2_grpc.ChatStub(self.channel)

    def send_message(self, msg):
        self.stub.SendMessage(chat_pb2.Message(msg=msg))

    def start_listening_thread(self):
        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        for msg in self.stub.Listen(chat_pb2.ListenRequest()):
            print(f">>> {msg.msg}")


def main():
    client = ChatClient()
    client.start_listening_thread()
    print("client initiated. Start chatting by typing anything and pressing enter.")
    while True:
        message = input()
        client.send_message(message)


if __name__ == "__main__":
    main()
