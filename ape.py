from pwn import *
import random
from datetime import datetime
random.seed(datetime.now().timestamp())
hands = ["rock", "paper", "scissors"]
loses = ["paper", "scissors", "rock"]

#print(i)
p = remote("saturn.picoctf.net", 51420)
#p = process("./game-redacted")
while True:
    print(p.recvuntil(b"Type '2' to exit the program\r\n"))
    p.sendline(b"1")
    print(p.recvuntil(b"Please make your selection (rock/paper/scissors):\r\n"))
    i = random.randint(0,2)
    a = bytes(f"{hands[i]}", 'utf-8')
    p.sendline(a)
print(p.recv())
#print(f'{loses[i]} {hands[i]}')
