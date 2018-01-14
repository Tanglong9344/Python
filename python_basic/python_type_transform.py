# type transform
str0 = 'Tanglong'   # string
print("str0=", str0)

i = int(65.31415)
print("i=", i)

f = float(i)        # to float
print("f=", f)

oct0 = oct(i)
print("oct=", oct0)  # to octonary

hex0 = hex(i)
print("hex=", hex0)  # to hexadecimal

ch = chr(i)
print("ch=", ch)  # to char

ii = ord(ch)
print("ii=", ii)  # to number

c = complex(3, 2)  # complex
print("c=", c)

tup = tuple(str0)
print("tup=", tup)

list0 = list(str0)
print("list0=", list0)

s = set(str0)
print("s=", s)

frozens = frozenset(str0)
print("frozens=", frozens)

dic = dict([(1, "One"), (2, "Two")])
print("dic=", dic)


class Createobj:
    pass


obj = Createobj()  # object
print("obj=", obj)

exp = repr(obj)
print("exp=", exp)
