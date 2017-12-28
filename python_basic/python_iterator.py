# Iterator
list = [1,2,3,4,5,6,7,8,9,0]
it = iter(list)
print("it=", it)
# traverse--1
for x in it:
    print(x, end=' ')
print()

# traverse--2
import sys
it = iter(list)
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        # sys.exit()
        break
print()

# define iterator
class Pow2Iterator:
    """Class to implement an iterator
    of powers of two"""

    # the max
    def __init__(self, max = 0):
        self.max = max

    # initialize n to 0
    def __iter__(self):
        self.n = 0
        return self

    # next transform
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

pow = Pow2Iterator(5)
it = iter(pow)
print("Pow2Iterator:")
while True:
    try:
        print(next(it), end=',')
    except StopIteration:
        break
