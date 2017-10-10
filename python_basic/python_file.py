#文件操作1
print ("文件操作1:")
fp = open("test.txt") #默认只读方式打开
data = fp.read()
print (data)
fp.close()

#文件操作2
print ("文件操作2:")
fp = open("test.txt")
data = fp.readline()
print (data)
fp.close()

#文件操作3
print ("文件操作3:")
fp = open("test.txt","r")
data = fp.readlines()
print (data)
fp.close()

#文件操作4-1
print ("文件操作4-1:")
fp = open("test.txt","a")  # a(appendind)不删除原始数据，直接在其后添加数据
fp.write("I am appending!\n")
fp.close()
fp = open("test.txt")
print (fp.read())
fp.close()

#文件操作4-2之写入
print ("文件操作4-2之写入:")
fp = open("test.txt","w") # w(writting)删除原始数据重新写入数据
#写入数据
fp.write("I am writting!\n")
fp.close()
fp = open("test.txt")
print (fp.read())
fp.close()