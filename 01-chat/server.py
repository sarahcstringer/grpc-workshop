from concurrent import futures
import grpc
import chat_pb2_grpc
import chat_pb2

messages = []
peer_to_username = {}

class ChatService(chat_pb2_grpc.ChatServicer):
    def ListChannels(self, request, context):
        return chat_pb2.ListChannelsResponse(channels=channels)

    def SendMessage(self, request, context):
        messages.append(request)
        return chat_pb2.MessageResponse(msg="Sent message")

    def Listen(self, request, context):
        peer = context.peer()
        seen_messages = len(messages)
        while True:
            if len(messages) > seen_messages:
                message = messages[seen_messages]
                seen_messages += 1
                if message.msg.startswith("@"):
                    username = message.msg.split()[0].strip('@')
                    if peer_to_username[peer] != username:
                        continue
                yield message

    def AddUser(self, request, context):
        username = request.username
        if username in peer_to_username.values():
            return chat_pb2.MessageResponse(msg="Username taken, choose another.")
        peer = context.peer()
        peer_to_username[peer] = username
        return chat_pb2.MessageResponse(msg="User added.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
