#if
str="hello"
if str == "Hello":
    print ("Yes!")
else :
    print ("No!")
print ()

#elif
from random import randint
x=randint(1,40)
if x == 1:
    print ("X is One")
elif x == 2:
    print ("X is Two")
elif x == 3:
    print ("X is Three")
elif x == 4:
    print ("X is Four")
else:
    print ("The range is too huge!")
print ("The X is :%d" %x)
print()

# nested if open-up and shut-down circuit
a=randint(0,1)
b=randint(0,1)
if a>0:
    if b>0:
        print ("open")
    else:
        print ("shutdown")
else:
    print ("shutdown")
print ("a: %d, b: %d" %(a,b))