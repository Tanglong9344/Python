# file1
print ("file-1:")
fp = open("test.txt") #open in read-only mode
data = fp.read()
print (data)
fp.close()

#file-2
print ("file-2:")
fp = open("test.txt")
data = fp.readline() # read only one line
print (data)
fp.close()

#file-3
print ("file-3:")
fp = open("test.txt", "r")
data = fp.readlines() # read all lines
print (data)
fp.close()

#file-4-1
print ("file-4-1:")
fp = open("test.txt","a")  # a(appendind)append data after old data
fp.write("I am appending!")
fp.close()
fp = open("test.txt")
print (fp.read())
fp.close()

#file-4-2
print ("file-4-2:")
fp = open("test.txt","w") # w(writting)writing over old data
fp.write("I am Tanglong.\nI am coding...")
fp.close()
fp = open("test.txt")
print (fp.read())
fp.close()