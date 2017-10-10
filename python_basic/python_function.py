#定义一个无参数函数
def hello():
    print("Hello!")

#调用函数
hello()

#定义一个带一参数函数
def mysum(n):
    s=0
    for i in range (1,n):
        s+=i;
    return s;

#调用函数
print (mysum(11))

#定义一个带两参数函数
def myadd(a,b):
    print(a+b)

#调用函数
myadd(1,3)

#为函数指定默认值
def hello (name = 'World!'):
    print ("Hello " + name)  #当函数未传递参数时使用默认值

hello()
hello("Python!")