# ESC
print("ESC: ")
print("\t hello \t world!\n")
print(r"\t hello \tworld! \n")  # r 表示不对字符串中的转义字符做处理
print(R"\t hello \tworld! \n")  # r 表示不对字符串中的转义字符做处理

# regular expression-1
# --1
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

text = "Hi, my name is Tanglong, Merry Christmas.welcome to Python,let me show you around."
# match-group
machList = re.match(r'(.*) is (.*?) .*',text,re.I)
if machList:
    print("searchList.group(): ",machList.group())
    print("searchList.group(1): ", machList.group(1))
    print("searchList.group(2): ", machList.group(2))
else:
    print("Not match...")
    
# seerch-group
searchList = re.search(r'(.*) is (.*?) .*',text,re.I)
if searchList:
    print("searchList.group(): ",searchList.group())
    print("searchList.group(1): ", searchList.group(1))
    print("searchList.group(2): ", searchList.group(2))
else:
    print("Not match...")

# match vs search
str    = "family"
subStr = "am"
print(re.match(subStr,str))  # match from the start position of the str
print(re.search(subStr,str)) #search through the str and find the matching part

# replace
str = "he23l12lo56"
str = re.sub(r'\d', ',' ,str)
print(str)