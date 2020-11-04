from concurrent import futures

import chat_pb2
import chat_pb2_grpc
import grpc

MESSAGES = []


class ChatService(chat_pb2_grpc.ChatServicer):
    """Implementation for functions defined in chat.proto and stubbed in chat_pb2_grpc."""

    def SendMessage(self, request, context):
        """Receive a message from a client and add it to MESSAGES."""

        MESSAGES.append(request)
        return chat_pb2.MessageResponse(msg="Sent message")

    def Listen(self, request, context):
        """Send new messages to a client.

        Only sends new messages that have been sent since a client joins the chat.
        The client will not receive older messages beyond when they joined.
        """

        seen_messages = len(MESSAGES)
        while True:
            if len(MESSAGES) > seen_messages:
                message = MESSAGES[seen_messages]
                seen_messages += 1
                yield message


def serve():
    """Serve the service on port 50051 with threaded workers.

    This function uses `grpc.server` and server stubs generated in chat_pb2_grpc to
    receive protobuf requests from clients.
    """

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("server started")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
