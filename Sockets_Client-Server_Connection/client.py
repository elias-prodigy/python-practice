import socket


def client():
    sock = socket.socket()
    sock.connect(('localhost', 8070))

    while True:
        m = input('Hi Michale! Ask any question: ')
        sock.send(m.encode())
        data1 = sock.recv(1024)
        print(data1.decode('utf-8'))


if __name__ == '__main__':
    client()

