from concurrent import futures

import chat_pb2
import chat_pb2_grpc
import grpc

MESSAGES = []
PEER_TO_USERNAME = {}


class ChatService(chat_pb2_grpc.ChatServicer):
    def SendMessage(self, request, context):
        MESSAGES.append(request)
        return chat_pb2.MessageResponse(msg="Sent message")

    def Listen(self, request, context):
        peer = context.peer()
        seen_messages = len(MESSAGES)
        while True:
            if len(MESSAGES) > seen_messages:
                message = MESSAGES[seen_messages]
                seen_messages += 1
                username = self.strip_username_from_message(message)
                if username and PEER_TO_USERNAME[peer] != username:
                    continue
                yield message

    def AddUser(self, request, context):
        username = request.username
        if username in PEER_TO_USERNAME.values():
            return chat_pb2.MessageResponse(
                msg="Username taken, please choose another.",
            )
        peer = context.peer()
        PEER_TO_USERNAME[peer] = username
        return chat_pb2.MessageResponse(msg=f"Added user")

    @staticmethod
    def strip_username_from_message(message):
        username = None
        if message.msg.startswith("@"):
            username = message.msg.split()[0].strip("@")
        return username


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
