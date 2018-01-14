#  format output
ch = 'A'
print("%c" % ch)    # 字符

s = 'Python'
print("%s" % s)  # 字符串
i = -1024
print("%d" % i)     # 十进制整数
print("%5d" % i)    # 指定宽度
print("%i" % i)     # 带符号的十进制整数
print("%u" % i)     # 无符号的十进制整数
print("%f" % i)     # 十进制浮点数
print("%.2f" % i)   # 指定精度
print("%3.2f" % i)  # 指定宽度和精度
print("%e" % i)     # 科学计数
print("%E" % i)     # 科学计数
print("%o" % i)     # 八进制
print("%X" % i)     # 十六进制
print("%x" % i)     # 十六进制
print("%#o" % i)   # 八进制，添加前导符号
print("%#X" % i)   # 十六进制，添加前导符号
print("%#x" % i)   # 十六进制，添加前导符号
print("%-10d" % i)  # 左对齐
print("%+10d" % i)  # 右对齐
print("%010d" % i)  # 空位补0
