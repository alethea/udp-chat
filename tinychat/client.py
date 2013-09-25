# 9/23/2013
# Alethea Butler

import socket


class Client:
    def __init__(self, dest_addr=("127.0.0.1", 5280)):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dest_addr = dest_addr
        self.running = True

    def run(self):
        while self.running:
            try:
                message = bytes(input("Message? "), "UTF-8")
            except EOFError:
                self.running = False
                break
            if message:
                sent = self.sock.sendto(message, self.dest_addr)
                print("{0} bytes sent".format(sent))
            else:
                print("no message sent")

    def __del__(self):
        self.running = False
        try:
            self.sock.close()
        except socket.error as e:
            print(e)


if __name__ == "__main__":
    Client().run()
