# ESC
print("ESC: ")
print("\t hello \t world!\n")
print(r"\t hello \tworld! \n")  # r 表示不对字符串中的转义字符做处理

# regular expression-1
# --1
'''
re是python里的正则表达式模块。
findall是其中一个方法，
用来按照提供的正则表达式，
去匹配文本中的所有符合条件的字符串。
返回结果是一个包含所有匹配的list。
'''
import re

print("--1：")
text = "Hi,my name is Tanglong,Merry Christmas.welcome to Python,let me show you around."
m = re.findall("me", text)
if m:
    print(m)
else:
    print('Not found!')

# --2
print("--2：")
m = re.findall("[Mm]e", text)  # []表示满足[]内任意一个字符，这样可以匹配大小写
if m:
    print(m)
else:
    print('Not found!')

# --3
print("--3：")
m = re.findall(".", text)  # “.”在正则表达式中表示除换行符以外的任意字符。
if m:
    print(m)
else:
    print('Not found!')

# regular expression-2
import re
tel = "123456790qwww6 三哥———___wqqw6666677qwqwwq88888888qwqw 1456789000"

# --1
print("--1：")
num = re.findall("^1\d*[q]?", tel)  # ^1 表示以 1 开头
if num:
    print(num)
else:
    print("Not found!")

# --2
print("--2：")
import re
tel = "123456790qwww6 三哥———___wqqw6666677qwqwwq88888888qwqw 1456789000"
num = re.findall("_*\D+\d+", tel)  # 匹配符合条件的字符串
if num:
    print(num)
else:
    print("Not found!")

# --3
print("--3：")
import re
tel = "(021)88776543010-55667890025844533620571 66345673"
num = re.findall("\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}", tel)  # 电话号码匹配
if num:
    print(num)
else:
    print("Not found!")