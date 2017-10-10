#字符串的遍历
print ("字符串的遍历：")
str = "Hello World!"
for ch in str:
    print (ch)

#字符串索引和切片
print ("字符串索引：")
str = "Hello World!"
print (str[-1])
print (str[2])
print (str[3 : 7])
print (str[ : ])

#str[1] = 'a'
'''
与list不同的是，字符串不能通过索引访问去更改其中的字符。
word[1] = 'a'
这样的赋值是错误的。
'''