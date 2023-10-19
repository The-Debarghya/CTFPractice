#!/usr/bin/python3
import os
flag = b"\x13\x4a\xf6\xe1\x29\x7b\xc4\xa9\x6f\x6a\x87\xfe\x04\x66\x84\xe8\x04\x70\x84\xee\x04\x6d\x84\xc5\x28\x2d\xd7\xef\x29\x2d\xc9"

class XOR:
    def __init__(self):
        self.key = b"\x5b\x1e\xb4\x9a"
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    crypto = XOR()
    print ('Flag:', crypto.decrypt(flag).decode('utf-8'))

if __name__ == '__main__':
    main()
