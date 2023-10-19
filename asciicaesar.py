ascii_table = []
for i in range(32, 127):
    ascii_table.append(chr(i))

str = '42m{y!"%w2\'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0'
str2 = []
for j in range(32, 126):
    shift = j
    for i in str:
        ch = ascii_table[(ord(i) + shift) % len(ascii_table)]
        str2.append(ch)
    print("".join(str2))
    str2.clear()
