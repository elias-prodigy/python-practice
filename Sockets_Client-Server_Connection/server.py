import socket


def server():
    sock = socket.socket()
    sock.bind(('', 8070))
    sock.listen(2)
    conn1, addr1 = sock.accept()
    print('connected:', addr1)
    while True:
        data1 = conn1.recv(1024)
        if not data1:
            break
        conn1.send(data1.upper())


if __name__ == '__main__':
    server()


