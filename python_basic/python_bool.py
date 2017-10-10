# and && or
#示例1
print ("示例1：")
a = "AA"
b = "BB"
print (True and a or b) #选a
print ((False and a) or b)#选b

#示例2
print ("示例2：")
a = ""
b = "BB"
print ((True and a) or b) #选b
print ((False and a) or b)#选b

#示例3
print ("示例3：")
a = "AA"
b = "BB"
print (True and [a] or [b]) #选a
print (False and [a] or [b])#选b

#示例4
print ("示例4：")
a = ""
b = "BB"
print (True and [a] or [b]) #选a
print (False and [a] or [b])#选b