# traverse a string
print ("traverse a string: ")
str = "Hello Python!"
for ch in str:
    print (ch)

# index and section in a string
print ("index: ")
str = "Hello Python!"
print (str[-1])
print (str[2])
print (str[3 : 7])
print (str[ : ])
print(str * 3)      # print this string two times
print(str + ",Bye Python.")

# 操作字符串的内置方法
str = "i am Tanglong, I am from China."
print(str.capitalize()) # convert the first char to upper case
print(str.count('a'))   # calculate the times of 'i'
print(str.find("am"))   # return index of "am"
print(str.index("am"))   # return index of "am"
print("123".isalnum())
print("abc".isalpha())
print("abc".islower())
print("ABC".isupper())
print("123".isdigit())
print(len(str)) # the length of str
print(str.lower()) # to lower case
print(str.upper()) # to upper case
print(max(str)) # return the maximum char in str
print(str.rstrip()) # delete all the whitespace
print(str.split(',')) # splite str according to ','
print(str.swapcase()) # swap the case of str