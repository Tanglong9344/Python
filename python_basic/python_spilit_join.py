# string split
print ("--1：")
str = "I am Tanglong"
print (str.split())

#--2
print ("--2：")
str = "I a.m Tan.g.lo.n.g"
print (str.split('.'))

#--3
print ("--3：")
str = "aAaAaAa"
print (str.split('A'))

# join values in a list with the string
print ("--1：")
str = " "
list = ["I", "am", "Tanglong"]
print(list)
print (str.join(list))

#--2

print ("--3：")
list = ["I", "am", "Tanglong"]
print (",".join(list))