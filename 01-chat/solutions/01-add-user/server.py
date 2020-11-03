from concurrent import futures

import chat_pb2
import chat_pb2_grpc
import grpc

MESSAGES = []
USERS = set()


class ChatService(chat_pb2_grpc.ChatServicer):
    def SendMessage(self, request, context):
        MESSAGES.append(request)
        return chat_pb2.MessageResponse(msg="Sent message")

    def AddUser(self, request, context):
        username = request.username
        if username in USERS:
            return chat_pb2.MessageResponse(
                msg="Username taken, please choose another.",
            )
        USERS.add(username)
        return chat_pb2.MessageResponse(msg=f"Added user")

    def Listen(self, request, context):
        seen_messages = len(MESSAGES)
        while True:
            if len(MESSAGES) > seen_messages:
                message = MESSAGES[seen_messages]
                seen_messages += 1
                yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
