b1 = b'hello bytes'
print(type(b1))
print("b1:", b1)

b2 = bytes('hello bytes2', encoding='utf-8')
print(type(b2))
print("b2:", b2)
print(b2.decode('utf-8'))  # decode bytes
