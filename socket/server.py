import socket
import time
from threading import Thread

import requests
from services import is_valid_uuid


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)

    def listen_for_clients(self):
        print('Listening...')
        while True:
            client, addr = self.server.accept()
            print('Accepted Connection from: ' +
                  str(addr[0]) + ':' + str(addr[1]))
            Thread(target=self.handle_client, args=(client, addr)).start()

    def handle_client(self, client_socket, address):
        size = 1024
        receive = client_socket.recv(size)
        data = receive.decode('utf8')
        print('Received: ' + data + ' from: ' +
              str(address[0]) + ':' + str(address[1]))
        while True:
            try:
                if is_valid_uuid(data):
                    payload = {"code": data}
                    response = requests.post(
                        'http://0.0.0.0:8000/api/product/', data=payload)
                    if response.status_code == 404:
                        try:
                            client_socket.sendall(
                                bytes(
                                    "El codigo ingresado no existe en nuestar base de datos",
                                    encoding='utf8'))
                        except socket.error as e:
                            print("socket error: %s" % e)
                        client_socket.close()
                        print(f"Conection with {host}:{port} close")
                        return False
                    elif response.status_code == 200:
                        try:
                            client_socket.sendall(bytes(response.content))
                            time.sleep(5)
                            print('Reload data')
                            response = requests.post(
                                'http://0.0.0.0:8000/api/product/', data=payload)
                        except socket.error as e:
                            print("socket error: %s" % e)
                            client_socket.close()
                            print(f"Conection with {host}:{port} close")
                            return False
                else:
                    try:
                        client_socket.sendall(
                            bytes(
                                "El codigo %s es incorrecto" %
                                data, encoding='utf8'))
                    except socket.error as e:
                        print("socket error: %s" % e)
                    client_socket.close()
                    print(f"Conection with {host}:{port} close")
                    return False
            except socket.error:
                client_socket.close()
                print(f"Conection with {host}:{port} close")
                return False


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9999
    main = Server(host, port)
    # start listening for clients
    main.listen_for_clients()
