# 字符串的分割
#形式1
print ("形式1：")
str = "I am chinese"
print (str.split())

#形式2
print ("形式2：")
str = "I am an American.How about.我是中国人.你好."
print (str.split('.'))

#形式3
print ("形式3：")
str = "AAA"
print (str.split('A'))

# list的 聚合
#形式1
print ("形式1：")
str = " "
list = ["I", "am", "chinese"]
print(list)
print (str.join(list))

#形式2
print ("形式2：")
list = ["I", "am", "chinese"]
print (",".join(list))

#形式3
print ("形式3：")
list = ["I", "am", "chinese"]
print ("".join(list))