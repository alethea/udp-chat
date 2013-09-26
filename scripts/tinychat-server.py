#!/usr/bin/env python3
#
# 9/23/2013
# Charles O. Goddard

from tinychat.server import Server
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--hostname', type=str, default='0.0.0.0')
parser.add_argument('-p', '--port', type=int, default=5280)
parser.add_argument('-t', '--timeout', type=float, default=2.0)

args = parser.parse_args()

Server(bind_addr=(args.hostname, args.port)).run(timeout=args.timeout)
