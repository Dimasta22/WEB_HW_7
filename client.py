import socket


def client(host, port):
    with socket.socket() as sock:
        try:
            print('Successes connection!')
            sock.connect((host, port))
            message = input('>>> ')
            while message.lower().strip() != 'exit':
                sock.send(message.encode())
                data = sock.recv(1024).decode()
                print(f'Received massages: {data}')
                message = input('>>> ')
            print('Communication was successful')
        except ConnectionRefusedError:
            print('Server not enable!!!')
        except ConnectionResetError:
            print('Server dropped connection!!!')


if __name__ == '__main__':
    HOST = socket.gethostname()
    PORT = 5000
    client(HOST, PORT)