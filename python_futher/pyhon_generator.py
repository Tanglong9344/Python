# generator
def fibonacci(n):   # generator function
    a, b, counter = 1, 1, 1
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f is iterator object

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        break
print()

str0 = "Tanglong"


def revese_str(str00):
    length = len(str00)
    for i in range(length - 1, -1, -1):
        yield str0[i]


print(revese_str(str0))
