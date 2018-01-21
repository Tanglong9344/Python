# python package 'random'
import random

# --1, int
print("--1, int：")
num = random.randint(1, 10)
print(num)

# --2, float
print("--2, float：")
num = random.random()  # range in 0-1
print(num)

# --3, float
print("--3, float：")
num = random.uniform(1, 10)
print(num)

# --4
print("--4：")
list0 = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"]
num = random.choice(list0)  # select value from a list
print(num)

# --5
print("--5：")
num = random.randrange(1, 20, 3)  # 从1 到 10，间隔为 3的随机数
print(num)                       # 即从[1，4, 7, 10, 13, 16, 19]中选择

# --6
# 和--5等价
print("--6：")
num = random.choice(range(1, 20, 3))
print(num)

# --7
print("--7：")
list0 = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"]
num = random.sample(list0, 3)  # 从list随机选取3个元素组成一个新序列
print(num)
