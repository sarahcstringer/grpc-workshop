from concurrent import futures

import chat_pb2
import chat_pb2_grpc
import grpc

MESSAGES = []

class ChatService(chat_pb2_grpc.ChatServicer):
    def ListChannels(self, request, context):
        return chat_pb2.ListChannelsResponse(channels=channels)

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
                yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
