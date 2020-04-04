import sys

print(sys.getdefaultencoding())

s = "中文"
print("s:", s)
# encode
s_encode = s.encode("utf-8")
print("s_encode:", s_encode)
# decode
s_decode = s_encode.decode("utf-8")
print("s_decode:", s_decode)
