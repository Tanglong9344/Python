#break && continue 的使用
#break
while True:
    x = input("输入字符串q:退出)：")
    print (x)
    if x == 'q':
        break    #彻底跳出循环

#continue
while True:
    x = int(input("输入整数(110:退出)："))
    if x < 60:
        continue # 跳出本次循环
    print (x)
    if x == 110:
        break    #彻底跳出循环