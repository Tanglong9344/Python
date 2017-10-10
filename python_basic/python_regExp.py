# 正则表达式 1
# 转义问题
print("转义问题：")
print("\t hello \t world!\n")
print(r"\t hello \tworld! \n")  # r 表示不对字符串中的转义字符做处理

# 示例1
'''
re是python里的正则表达式模块。
findall是其中一个方法，
用来按照提供的正则表达式，
去匹配文本中的所有符合条件的字符串。
返回结果是一个包含所有匹配的list。
'''
print("示例1：")
import re
text = "Hi,my name is Merry,welcome to Github,let me show you around."
m = re.findall("me", text)
if m:
    print(m)
else:
    print('Not found!')

# 示例2
print("示例2：")
import re
text = "Hi,my name is merry,welcome to Github,let me show you around."
m = re.findall("[Mm]e", text)  # []表示满足[]内任意一个字符，这样可以匹配大小写
if m:
    print(m)
else:
    print('Not found!')

# 示例3
print("示例3：")
import re
text = "Hi,my name is merry,welcome to Github,let me show you around."
m = re.findall(".", text)  # “.”在正则表达式中表示除换行符以外的任意字符。
if m:
    print(m)
else:
    print('Not found!')

# 示例4
print("示例4：")
import re
text = "Hi,my name is merry,welcome to Github,let me show you around."
m = re.findall("\s", text)  # "\S"(大写的S）它表示的是不是空白符的任意字符
if m:
    print(m)
else:
    print('Not found!')

# 示例5
print("示例5：")
import re
text = "Hi,my name is merry,welcome to Github,let me show you around."
m = re.findall("\s", text)  # "\s"(小写的S）它表示的是空白符
if m:  # \大写字母 与 \小写字母 意思相反
    print(m)
else:
    print('Not found!')

# 示例6
print("示例6：")
import re
text = "Hi,my name is merry,welcome to Github,let me show you around."
print("示例6.1:")
m = re.findall(".*", text)  # “*”表示任意数量连续字符，这种被称为通配符。
if m:
    print(m)
else:
    print('Not found!')
print("示例6.2:")
m = re.findall("m.*", text)  # 以 m 开头的字符串
if m:
    print(m)
else:
    print('Not found!')

print("示例6.3:")
m = re.findall(".*y", text)  # 以 y 结尾的字符串
if m:
    print(m)
else:
    print('Not found!')

print("示例6.4:")
m = re.findall("m.*y", text)  # 以 m 开头，y结尾的字符串
if m:
    print(m)
else:
    print('Not found!')

print("示例6.5:")
m = re.findall(".*?", text)  # "?"表示符合条件的最短字符串
if m:
    print(m)
else:
    print('Not found!')

print("示例6.6:")
m = re.findall("m.*?", text)
if m:
    print(m)
else:
    print('Not found!')

print("示例6.7:")
m = re.findall(".*?y", text)
if m:
    print(m)
else:
    print('Not found!')

print("示例6.8:")
m = re.findall("m.*?y", text)
if m:
    print(m)
else:
    print('Not found!')

# 正则表达式2
# 示例1
print("示例1：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("[0123456789]", tel)
if num:
    print(num)
else:
    print("Not found!")

# 示例2
print("示例2：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("[0-9]", tel)  # 和示例 1 等价
if num:
    print(num)
else:
    print("Not found!")

# 示例3
print("示例3：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("[0-9]*", tel)  # 表示任意长度(包括0)
if num:
    print(num)
else:
    print("Not found!")

# 示例4
print("示例4：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("[0-9]+", tel)  # (长度大于0)
if num:
    print(num)
else:
    print("Not found!")

# 示例5
print("示例5：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("\d", tel)  # 和示例 1 等价
if num:
    print(num)
else:
    print("Not found!")

# 示例6
print("示例6：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("\d*", tel)  # 和示例 3 等价
if num:
    print(num)
else:
    print("Not found!")

# 示例7
print("示例7：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("\d+", tel)  # 和示例 4 等价
if num:
    print(num)
else:
    print("Not found!")

# 示例8
print("示例8：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("\d{6}", tel)  # { } 可以指定任意长度 \d{6} <==> [0-9]{6}
if num:
    print(num)
else:
    print("Not found!")

# 示例9
print("示例9：")
import re
tel = "12345678900qwwqqw677wqqw6666677qwqwwq8888888888888qwqw123456789000"
num = re.findall("\D{4}", tel)  # 非数字
if num:
    print(num)
else:
    print("Not found!")

# 示例10
print("示例10：")
import re
tel = "123456790qwww6三哥———___wqqw6666677qwqwwq88888888qwqw1456789000"
num = re.findall("\w{4}", tel)  # 字母或者数字或者下划线或者汉字
if num:
    print(num)
else:
    print("Not found!")

# 示例11
print("示例11：")
import re
tel = "123456790qwww6 三哥———___wqqw6666677qwqwwq88888888qwqw 1456789000"
num = re.findall("^1\d*[q]?", tel)  # ^1 表示以 1 开头
if num:
    print(num)
else:
    print("Not found!")

# 示例12
print("示例12：")
import re
tel = "123456790qwww6 三哥———___wqqw6666677qwqwwq88888888qwqw 1456789000"
num = re.findall("_*\D+\d+", tel)  # 匹配符合条件的字符串
if num:
    print(num)
else:
    print("Not found!")

# 示例13
print("示例13：")
import re
tel = "(021)88776543010-55667890025844533620571 66345673"
num = re.findall("\(0\d{2,3}\)\d{7,8} | 0\d{2,3}[ -]?\d{7,8}", tel)  # 电话号码匹配
if num:
    print(num)
else:
    print("Not found!")