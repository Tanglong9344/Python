# Iterator
list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
it = iter(list0)
print("it=", it)
# traverse--1
for x in it:
    print(x, end=' ')
print()

# traverse--2
it = iter(list0)
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
    def __init__(self, max0=0):
        self.max0 = max0

    # initialize n to 0
    def __iter__(self):
        self.n = 0
        return self

    # next transform
    def __next__(self):
        if self.n <= self.max0:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


pow0 = Pow2Iterator(5)
it = iter(pow0)
print("Pow2Iterator:")
while True:
    try:
        print(next(it), end=',')
    except StopIteration:
        break
