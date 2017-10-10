#使用 randint 产生一定范围内的随机数
from random import randint
num=randint(10,100) #产生10-100之间的随机数
answer = 101
while answer!=num:
    print ('Guess what I think?')
    answer = int(input())
    if answer<num:
    	print ('%d too small'% answer)
    if answer>num:
        print ('%d too big'% answer)
    if answer==num:
        print ('Bingo,You got the correct answer %d!' % answer)