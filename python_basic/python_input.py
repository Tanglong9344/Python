x = input("Please input a string: ")
print(x)

try:
    x = int(input("Please input a number: "))
except Exception as e:
    print('请输入整数')
    x = ''
print(x)

try:
    x = float(input("Please input a float: "))
except Exception as e:
    print('请输入数字')
    x=''
print(x)

x = str(input("Please input a string: "))
print(x)

try:
    x = bool(input("Please input a bool: "))
except Exception as e:
    print('请输入布尔值')
    x = ''
print(x)
