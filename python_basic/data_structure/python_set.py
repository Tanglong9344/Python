# set 集合--元素不重复--可利用此性质去重
s = {1, 2, 1, 2, "set1", True, (4, 5, 6)}
print("set=", s)

# add
s.add("addElement")
print("set=", s)

# remove
s.remove(1)
print("set=", s)

s2 = {33, 44, 55, 66}

# union
print("union:", s.union(s2))

# return differenceF of two sets
print(s.difference(s2))

# 数据添加
datas = {}
print(datas.get(1))
print(datas.get(2))
print(datas.get(4))
data = datas.get(4)
if data is None:
    data = []
a = {'a': '11', 'b': '22'}
data.append(a)
datas[4]=data
print(datas.get(4))