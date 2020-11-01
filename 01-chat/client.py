import grpc
import chat_pb2_grpc
import chat_pb2
import threading


class ChatClient(object):
    def __init__(self, host="localhost", port="50051"):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.stub = chat_pb2_grpc.ChatStub(self.channel)
    

    def add_user(self, username):
        user = chat_pb2.User(username=username)
        response = self.stub.AddUser(user)
        self.user = user
        return response

    def send_message(self, msg):
        self.stub.SendMessage(chat_pb2.Message(msg=msg, user=self.user))

    def start_listening_thread(self):
        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        for msg in self.stub.Listen(chat_pb2.ListenRequest()):
            print(f">>> from {msg.user.username}: {msg.msg}")




### MENU COMMANDS

def main():
    client = ChatClient()
    username = input("choose a username >>> ")
    client.add_user(username)

    # TODO: Create a new user before starting chat

    client.start_listening_thread()
    while True:
        message = input()
        client.send_message(message)


if __name__ == "__main__":
    main()
