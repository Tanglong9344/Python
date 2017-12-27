#for
n = 11
s=0
for i in range (1,n):
    print(i,end='')
    if i<n-1:
        print('+', end='')
    s += i
print("=", end='')
print(s)

#while
s=0
i=1
while i<n:
    print(i, end='')
    if(i<n-1):
        print('+',end='')
    s += i
    i += 1
print("=%d" % s)

# Iterator
list = [1,2,3,4,5,6,7,8,9,0]
it = iter(list)
print("it=", it)
# traverse--1
for x in it:
    print(x, end=' ')
print()
# traverse--2
import sys
it = iter(list)
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        # sys.exit()
        break
print()

# generator
import sys
def fibonacci(n): #generator function
   a, b, counter = 1, 1, 1
   while True:
      if (counter > n):
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(10) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()