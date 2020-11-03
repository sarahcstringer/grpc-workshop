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

    def add_user(self, username):
        user = chat_pb2.User(username=username)
        response = self.stub.AddUser(user)
        print(response.msg)
        if response.msg == "Added user":
            self.user = user
            return True
        return False

    def send_message(self, msg):
        self.stub.SendMessage(chat_pb2.Message(msg=msg, user=self.user))

    def start_listening_thread(self):
        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        for msg in self.stub.Listen(chat_pb2.ListenRequest()):
            print(f">>> {msg.user.username}: {msg.msg}")


### MENU COMMANDS


def main():
    client = ChatClient()

    while True:
        username = input("choose a username >>> ")
        added_user = client.add_user(username)
        if added_user:
            break

    client.start_listening_thread()
    while True:
        message = input()
        client.send_message(message)


if __name__ == "__main__":
    main()
