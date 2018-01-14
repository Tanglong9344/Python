# and && or

print("--1：")
a = "AA"
b = "BB"
print(True and a or b)     # a selected
print((False and a) or b)  # b selected

print("--2：")
a = ""
b = "BB"
print((True and a) or b)   # b selected
print((False and a) or b)  # b selected

print("--3：")
a = "AA"
b = "BB"
print(True and [a] or [b])   # a selected
print(False and [a] or [b])  # b selected

print("--4：")
a = ""
b = "BB"
print(True and [a] or [b])   # a selected
print(False and [a] or [b])  # b selected
