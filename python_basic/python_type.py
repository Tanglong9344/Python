# Basic type in python
print("单一赋值：")
i = 110          # 整型
print(type(i))
print("i=",  i)
print("0x110=", 0x110)
print("0o110=", 0o110)

f = 9.99         # 浮点数
print(type(f), end=', ')
print(f)

c = 2 + 3j      # 复数
print(type(c), end=', ')
print(c)

str0 = "Tanglong"  # 字符串
print(type(str0), end=', ')
print(str0)

b = True        # 布尔值
print(type(b), end=', ')
print(b)

print("多重赋值：")
i2, f2, str2, b2, c2 = 1101, 9.999, "Tanglongg", False, 2j+3
print(i2, end=', ')
print(f2, end=', ')
print(str2, end=', ')
print(b2, end=', ')
print(c2)
