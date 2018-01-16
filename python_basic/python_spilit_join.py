# string split
print("--1：")
str0 = "I am Tanglong"
print(str0.split())

# --2
print("--2：")
str0 = "I a.m Tan.g.lo.n.g"
print(str0.split('.'))

# --3
print("--3：")
str0 = "aAaAaAa"
print(str0.split('A'))

# join values in a list with the string
print("--1：")
str0 = " "
list0 = ["I", "am", "Tanglong"]
print(list0)
print(str0.join(list0))

# --2
print("--3：")
list0 = ["I", "am", "Tanglong"]
print(",".join(list0))
