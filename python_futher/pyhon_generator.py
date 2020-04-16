def fibonacci(n):
    a, b, counter = 1, 1, 1
    while counter < n:
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

str = "TangLong"
print('---------return-------------')
def return_str(str):
    length = len(str)
    result = []
    for i in range(length):
        if str[i].islower():
            result.append(str[i])
    return result

print(return_str(str))
str2 = return_str(str)
for i in str2:
    print(i,end=',')
print()

print('---------yield-------------')
def yield_str(str):
    length = len(str)
    for i in range(length):
        if str[i].islower():
            yield str[i]

print(yield_str(str))
iter = yield_str(str) # will be cleared after visiting
print('------iteration-------')
while True:
    try:
        print(next(iter), end=",")
    except StopIteration:
        break
# for i in iter:
#     print(i,end=',')
# print()