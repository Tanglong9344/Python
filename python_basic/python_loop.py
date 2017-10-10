#for 循环使用 (a.单行注释使用# b.多行注释使用''' ''')
s=0
for i in range (1,11):
    print(i,end=' ')
    if i<10:
        print('+',end=' ')
    s+=i
print()
print("for:1+....+10=",end=' ')
print(s)

# print () 会自动换行，如果不想它换行，可以添加end=' '如下所示，print("hello",end='')
print("Hello")
print("World!")

print("Hello",end=' ')
print("World!")

#while 循环使用
s=0
i=1
while i<11:
    print(i,end='')
    if(i<10):
        print('+',end='')
    s+=i
    i=i+1
print("=%d" % s)