# 字典
# 格式 {key(键) : value(值)}
# 1.键必须是唯一的；
# 2.键只能是简单对象，比如字符串、整数、浮点数、bool值。
# 3.list就不能作为键，但是可以作为值。

# --1
print('--1：')
score = {
    'A': 30,
    'tanglong': 98,
    12: 66,
    12.22: 77,
    False: 78,
}
print(score)
print(str(score))
print(score['tanglong'])
print('keys: ', score.keys())
print('values: ', score.values())
print('length=', len(score))
print('length=', score.__len__())
print(type(score))

for name in score:  # traverse the score
    print(name, end=':')
    print('%d' % score[name], end=', ')

print('--2：')
score['tanglong'] = 100  # modification
score['LiuBei'] = 89     # add
del score[12.22]          # delete

for name in score:
    print(name, end=':')
    print('%d' % score[name], end=', ')
print('\n')

# --3
print('--3：')
dic = {}
# dic[2] = 22
print(dic)
dic.clear()  # clear dic2
print(dic)
