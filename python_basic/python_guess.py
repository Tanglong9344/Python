from random import randint

num = randint(10, 100)  # 产生10-100之间的随机数
cnt = 0
while True:
    print('Please input a number: ')
    try:
        answer = int(input())
        cnt += 1
    except Exception as e:
        print('请输入整数')
        continue
    if answer < num:
        print('%d is too small...' % answer)
    if answer > num:
        print('%d is too big...' % answer)
    if answer == num:
        print('Bingo, You got the correct answer %d!' % answer)
        print('You have guessed %d times.'% cnt)
        break
