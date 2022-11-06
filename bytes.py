s = '0x5FABFF01'
b = s.encode('utf-8')
# print(type(b))

# by = ''.join(format(ord(x), '08b') for x in s)
# print(by)

new = bytearray(b)
print(new)
print(new[0])
print(new[7])
print(new[1], new[2], new[3], new[4])
