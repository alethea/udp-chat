# 9/23/2013
# Charles O. Goddard

import socket

import sys

class Server:
    def __init__(self, bind_addr=("127.0.0.1", 5280)):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bsock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.bsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind_addr = bind_addr
        self.running = False

    def run(self, timeout=2.0):
        self.running = True
        self.sock.bind(self.bind_addr)
        self.bsock.bind(('', 0))
        self.sock.settimeout(timeout)
        while self.running:
            try:
                message, address = self.sock.recvfrom(1024)
                s = "Message from %r: %s" % (address, message)
                self.bsock.sendto(s.encode("UTF-8"), ('<broadcast>', self.bind_addr[1]))
                print(s)
            except socket.timeout:
                print(".", end="")
                sys.stdout.flush()
                continue
            except socket.error as e:
                print(e)
                break
            except KeyboardInterrupt:
                print("I can see when I\'m not wanted.")
                break

    def __del__(self):
        self.running = False
        try:
            self.sock.close()
            self.bsock.close()
        except socket.error as e:
            print(e)
