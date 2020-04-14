list_common = []
for i in range(1, 5):
    list_common.append(i)

print("list_common:", list_common)

# list comprehension
list_compre = [i for i in range(1, 5)]
print("list_compre:", list_compre)

a = [i**2 for i in range(1, 5)]
print("a=", a)
b = [j+1 for j in range(1, 5)]
print("b=", b)
c = [n for n in range(1, 10) if n % 2 == 0]
print("c=", c)
d = [letter.lower() for letter in 'ABCDEFG']
print("d=", d)
e = {i: i + 1 for i in range(4)}
print("e=", e)
f = {i: j for i, j in zip(range(1, 6), 'abcde')}
print("f=", f)
g = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}
print("g=", g)

# visit two lists at the same time
for a, b in zip(list_common, list_compre):
    print(a, '&&', b, end=", ")
print()

# sorted
print("sorted:", sorted(list_common))

# sorted--reversed
print("sorted:", sorted(list_common, reverse=True))

# enumerate
letters = ['a', 'b', 'c', 'd', 'e']
for num,letter in enumerate(letters):
    print(letter,'is',num + 1, end=",")
print()