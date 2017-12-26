#for (a.单行注释使用# b.多行注释使用''' ''')
s=0
for i in range (1,11):
    print(i,end=' ')
    if i<10:
        print('+', end=' ')
    s += i
print(" = ", end='')
print(s)

#while
s=0
i=1
while i<11:
    print(i, end='')
    if(i<10):
        print('+',end='')
    s += i
    i += 1
print(" = %d" % s)