# 9/23/2013
# Alethea Butler

import socket
import threading


class Client:
    def __init__(self, dest_addr=("127.0.0.1", 5280), listen_addr=("127.0.0.1", 5281)):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dest_addr = dest_addr
        self.listen_addr = listen_addr
        self.running = True
        self.thread = None

    def recvthread(self):
        self.bsock.bind(self.listen_addr)
        self.bsock.settimeout(2)
        while self.running:
            try:
                message, address = self.bsock.recvfrom(1024)
            except socket.timeout:
                continue
            print(message.decode('UTF-8'))

    def run(self):
        self.thread = threading.Thread(target=self.recvthread)
        self.thread.start()
        self.sock.settimeout(None)

        while self.running:
            try:
                message = bytes(input("Message? "), "UTF-8")
            except EOFError:
                print('\nDone')
                self.running = False
                self.thread.join()
                break
            if message:
                sent = self.sock.sendto(message, self.dest_addr)
                print("{0} bytes sent".format(sent))
            else:
                print("no message sent")

    def __del__(self):
        self.running = False
        self.thread.join()
        try:
            self.sock.close()
        except socket.error as e:
            print(e)


if __name__ == "__main__":
    Client().run()
