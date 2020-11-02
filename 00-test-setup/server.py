import concurrent

import grpc
import test_setup_pb2
import test_setup_pb2_grpc


class TestSetupService:
    def Request(self, request, context):
        print("Received request from gRPC client.")
        return test_setup_pb2.Response(message="Setup successful!")


def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=1))
    test_setup_pb2_grpc.add_TestSetupServicer_to_server(TestSetupService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server is running.")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
