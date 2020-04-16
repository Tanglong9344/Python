fp = open("test.txt")  # open in read-only mode
data = fp.read()
print(data)
fp.close()

fp = open("test.txt")
data = fp.readline()  # read only one line
print(data)
fp.close()

try:
    fp = open("test.txt", "r")
    data = fp.readlines()  # read all lines
    print(data)
except Exception as e:
    print('open file failed:',e)
    fp = open("test.txt", "w")
fp.close()


fp = open("test.txt", "a")  # a(appendind)append data after old data
fp.write("I am appending!")
fp.close()
fp = open("test.txt")
print(fp.read())
fp.close()

fp = open("test.txt", "w")  # writing over old data
fp.write("I am Tanglong.\nI am coding...")
fp.close()

# read
fp = open("test.txt", encoding="utf-8")
print("mode: ", fp.mode)
print("name: ", fp.name)
print("encoding: ", fp.encoding)
print("position: ", fp.tell())
print("content:\n", fp.read())
print("position: ", fp.tell())
fp.close()