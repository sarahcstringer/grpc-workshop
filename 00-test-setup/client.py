import grpc
import test_setup_pb2
import test_setup_pb2_grpc


class Client(object):
    def __init__(self, host="localhost", port="50051"):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.stub = test_setup_pb2_grpc.TestSetupStub(self.channel)

    def run(self):
        message = self.stub.Request(test_setup_pb2.EmptyRequest())
        print(message.message)


if __name__ == "__main__":
    c = Client()
    c.run()
