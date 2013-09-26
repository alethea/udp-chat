#!/usr/bin/env python3
#
# 9/25/2013
# Alethea Butler

from tinychat.client import Client
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, default=5280)
parser.add_argument('-l', '--localport', type=int, default=5281)
parser.add_argument('-I', '--interface', type=str, default='0.0.0.0')
parser.add_argument('hostname', type=str, nargs='?', default='127.0.0.1')

args = parser.parse_args()

Client(dest_addr=(args.hostname, args.port), listen_addr=(args.interface, args.localport)).run()
