import socket, sys, time


def main():
    target_host = '127.0.0.1'
    target_port = 9999

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Could not create a socket')
        time.sleep(1)
        sys.exit()

    try:
        client.connect((target_host, target_port))
    except socket.error:
        print('Could not connect to server')
        time.sleep(1)
        sys.exit()

    msg = input("> ")
    online = True
    while online:
        try:
            client.sendall(bytes(msg, encoding='utf8'))
            message = client.recv(4096)
            if message:
                print('[+] Received: ' + message.decode())
        except socket.error as e:
            client.close()
            print(f"Conection close by server")
            return False
        if 'q^' in message.decode('utf8'):
            client.close()
            online = False
            break

# start client
main()