import string

a = "1412 1404 1421 1407 1460 1452 1386 1414 1449 1445 1388 1432 1388 1415 1436 1385 1405 1388 1451 1432 1386 1388 1388 1392 1462"
a = a.split()

char = ""
for c in (chr(i) for i in range(32, 127)):
    char += c

print(char)
fl = ""
count = 0

for i in a:
    count = int(i)-1369
    fl += char[count]
print(fl)
