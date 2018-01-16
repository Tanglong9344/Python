# import module 'string'
import string

# traverse a string
print("traverse a string: ")
str0 = "Hello Python!"
for ch in str0:
    print(ch)

# index and section in a string
print("index: ")
str0 = "Hello Python!"
print(str0[-1])
print(str0[2])
print(str0[3:7])
print(str0[:])
print(str0 * 3)      # print this string two times
print(str0 + ", Bye Python.")

# 操作字符串的内置方法
str0 = "i am Tanglong, I am from China."
print(str0.capitalize())  # convert the first char to upper case
print(str0.count('a'))    # calculate the times of 'i'
print(str0.find("am"))    # return index of "am"
print(str0.index("am"))   # return index of "am"
print("123".isalnum())
print("abc".isalpha())
print("abc".islower())
print("ABC".isupper())
print("123".isdigit())
print(len(str0))        # the length of str
print(str0.lower())     # to lower case
print(str0.upper())     # to upper case
print(max(str0))         # return the maximum char in str
print(max(str0))        # return the maximum char in str
print(str0.rstrip())    # delete all the whitespace
print(str0.split(','))  # splite str according to ','
print(str0.swapcase())  # swap the case of str

str0 = "StringMultiply" * 3
print(str0)

# all the punctuations
print(string.punctuation)
# digit
print(string.digits)
# whitespace
print(string.whitespace)
# all the letters
print(string.ascii_letters)
# letter in lowercase
print(string.ascii_lowercase)
# letter in uppercase
print(string.ascii_uppercase)
# hexadecimal digits
print(string.hexdigits)
# octal digits
print(string.octdigits)
