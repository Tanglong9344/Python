import sys
print(sys.getdefaultencoding())# default encoding

s = "中文"
print("s:",s)
s_encode = s.encode("utf-8")
print("s_encode:",s_encode)
s_decode = s_encode.decode("utf-8")
print("s_decode:",s_decode)