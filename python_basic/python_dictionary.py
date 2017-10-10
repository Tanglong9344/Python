# 字典
# 格式 {key(键) : value(值)}
# 1.键必须是唯一的；
# 2.键只能是简单对象，比如字符串、整数、浮点数、bool值。
# 3.list就不能作为键，但是可以作为值。
# ex1
print("示例1：")
score = {
    "A": 30,
    "tanglong": 98,
    12: 66,
    12.22: 77,
    False: 78
}

for name in score:  # 字典的遍历
    print(name, end='')
    print(": %d" % score[name])

print("示例2：")
score["tanglong"] = 100  # 更改
score["刘备"] = 89  # 增加
del score[12.22]  # 删除

for name in score:  # 字典的遍历
    print(name, end='')
    print(": %d" % score[name])
print("\n")

# 新建一个空字典
print("示例3：")
dic = {}
dic[22] = 22
print(dic[22])