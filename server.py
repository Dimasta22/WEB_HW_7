import socket
import faker
from concurrent.futures import ThreadPoolExecutor


faker = faker.Faker()
OBJECTS = 5


def worker(sock: socket.socket, address: str):
    print(f'Connection from {address}\n')
    while True:
        message = sock.recv(1024).decode()
        if not message:
            break
        print(f'Received massages from {faker.name()}: {message}')
        data = input('>>> ')
        sock.send(data.encode())
    print(f'Socket connection closed {address}')
    sock.close()


def server(host, port):
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(OBJECTS)
    print(f'Start our server {server_socket.getsockname()}')
    with ThreadPoolExecutor(OBJECTS) as client_pool:
        try:
            while True:
                conn, address = server_socket.accept()
                client_pool.submit(worker, conn, address)

        except KeyboardInterrupt:
            print(f'Destroy server')
        finally:
            server_socket.close()


if __name__ == '__main__':
    HOST = socket.gethostname()
    PORT = 5000
    server(HOST, PORT)