from pwn import *
d = {}
d[0] = 1096770097
d[1] = 1952395366
d[2] = 1600270708
d[3] = 1601398833
d[4] = 1716808014
d[5] = 1734291511
d[6] = 960049251
d[7] = 1681089078
print(d)
l = []
hexBytes = []
for i in range(8):
    print(p32(d[i], endian="big").decode("utf-8"), end="")
