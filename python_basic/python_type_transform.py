# type transform
str = 'Tanglong'   # string
print("str=", str)

i   = int(65.31415)
print("i=", i)

f = float(i)        # to float
print("f=", f)

oct = oct(i)
print("oct=", oct) # to octonary

hex = hex(i)
print("hex=", hex)# to hexadecimal

ch = chr(i)
print("ch=", ch)  # to char

ii = ord(ch)
print("ii=", ii) # to number

c = complex(3,2) # complex
print("c=", c)

tup = tuple(str)
print("tup=", tup)

l = list(str)
print("l=", l)

s = set(str)
print("s=", s)

frozens = frozenset(str)
print("frozens=", frozens)

dic = dict([(1,"One"),(2,"Two")])
print("dic=", dic)

class Createobj:
    pass
obj = Createobj() # object
print("obj=", obj)

exp = repr(obj)
print("exp=", exp)