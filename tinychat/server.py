# 9/23/2013
# Charles O. Goddard

import socket

import sys

class Server:
    def __init__(self, bind_addr=("0.0.0.0", 5280), client_port=5281):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind_addr = bind_addr
        self.client_port = client_port
        self.running = False
        self.clients = []

    def run(self, timeout=2.0):
        self.running = True
        self.sock.bind(self.bind_addr)
        self.sock.settimeout(timeout)
        while self.running:
            try:
                raw_message, address = self.sock.recvfrom(1024)
                if not address[0] in self.clients:
                    self.clients.append(address[0])

                message = raw_message.decode('UTF-8')
                s = "[%s]: %s" % (address[0], message)
                print(s)

                data = s.encode('UTF-8')
                for cl in self.clients:
                    #if cl == address[0]:
                    #    continue
                    self.sock.sendto(data, (cl, self.client_port))

            except socket.timeout:
                continue
            except socket.error as e:
                print(e)
                break
            except KeyboardInterrupt:
                print("\nI can see when I\'m not wanted.")
                break

    def __del__(self):
        self.running = False
        try:
            self.sock.close()
        except socket.error as e:
            print(e)
