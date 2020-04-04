str = ' hello python! '
for ch in str:
    print(ch, end=',')
print()

print(str[-1])  # 末位
print(str[2])
print(str[3:7]) # 不包含7
print(str[:])
print(str * 2)
print(str + "Bye Python.")
print(str.capitalize())  # the first letter to upper case
print(str.count('l'))    # times of 'l'
print(str.find("l"))     # index of the first position of 'l'
print(str.index("lo"))   # index of the first position of "lo"
print("123".isalnum())
print("123".isdigit())
print("abc".isalpha())
print("abc".islower())
print("ABC".isupper())
print(len(str))
print(str.lower())
print(str.upper())
print(max(str))
print(min(str))
print(str.rstrip()) # 删除末尾空格
print(str.swapcase())

# single quotes
str1 = 'Hello single quotes'
print('str1=', str1)
# double quotes
str2 = "Hello double quotes"
print('str2=', str2)
# triple quotes--support multi-lines string
str3 = '''
triple
quotes
'''
print('str3=', str3)

# escape sequences
str4 = 'Hello, I\'m Tanglong'
print('str4=', str4)
# backslash
str5 = 'Hello ' \
       'backslash'
print('str5=', str5)
# raw strings(转义字符无效)
str6 = r'This is a \t raw string \n'
print('str6=', str6)
# unicode string
str7 = u'This is a unicode string'
print('str7=', str7)
# string literal concatenation
str8 = 'Hello\t' 'concatenation'
print('str8=', str8)

# split
str2 = "He.llo py.th.on"
print(str2.split())
print(str2.split('.'))
print(str2.split('a'))

# join
str = ' '
l = ['I', 'am', 'Tang','long']
print(l)
print(str2.join(l))
print(",".join())