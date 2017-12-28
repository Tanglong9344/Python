# python Exception

# assert
a = 5
assert a>3
print("Going...")

# try-except-finally
try:
    f = open('non-exist.txt')
    print ('File opened.')
    f.close()
except:
    print ('File not find...')
finally:
    print("Done.")

# try-except Exception
a = 3
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print("Zero can not be a divisor!")

# raise
if(b == 0):
    raise ZeroDivisionError("Zero can not be a divisor!")
else:
    print(a/b)