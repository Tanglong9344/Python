# Python package 'os'

import os
print("os.name:", os.name)
print("os.getcwd():", os.getcwd())
print("os.curdir:", os.curdir)

# use the built-in dir function to list the identifiers that a module defines.
print(dir(os))
a = 12
xx = 'test'
print(dir())  # list the identifiers of current module
print(dir(dir))  # list the identifiers that dir module defines
