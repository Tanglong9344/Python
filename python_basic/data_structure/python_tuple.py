# python tuple，元组-can not be modified
tuple0 = (3, 6.2828, True, "TUPLE")
print(tuple0[0])
print(tuple0[-1])
print(tuple0[1:-1])
print("length: %d" % tuple0.__len__())
print("length:", tuple0.__len__())
print(tuple0 * 3)

# tuple with a single element
tuple1 = (3,)  # and (3) means a object surrounded by a pair of parentheses
print(tuple1[0])
# empty tuple
tuple2 = ()
print(tuple2)

# format output
tuple3 = (23, "format", "output", 33)
print("%d, %s, %s, %d" % tuple3)