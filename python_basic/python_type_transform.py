# to int
i = int(65.31415)
print('int:', i)
# to float
print('float:', float(i))
# to octonary
print('oct:', oct(i))
# to hexadecimal
print('hex:', hex(i))
# to char
print('chr:', chr(i))
# to number
print('ord::', ord('A'))
# to complex
print('complex:', complex(3, 2))
# string
str = 'Tang long'
print('str:', str)
# tuple
print('tuple:', tuple(str))
# list
print('list:', list(str))
# set
print('set:', set(str))
# frozenset
print('frozenset:', frozenset(str))
# dict
print('dict:', dict([(1, 'One'), (2, 'Two')]))
# object
class CreateObject:
    pass

print('object:',CreateObject() )
# repr(object to string)
print('repr  :', repr(CreateObject()))
