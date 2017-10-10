#原文件数据
'''
#-- scores.txt
刘备 23 35 44 47 66
关羽 60 77 68
张飞 97 99 89 91
诸葛亮 100
曹操 
'''
#文件数据处理
fpin = open("scores.txt",encoding='utf-8')#以utf-8编码打开
lines = fpin.readlines()
fpin.close()
print (lines)

results = []

for line in lines[ : ]:
    l = line.split()
    print (l)
    sum = 0
    for score in l[1 : ]:
        sum += int(score)
    result = ("%s's score is : %d\n" %(l[0], sum))

#计算每个人的分数
    results.append(result)

#将结果写入results.txt
fpout = open("result.txt", "w",encoding='utf-8')
fpout.writelines(results)
fpout.close()      

#处理后文件数据 results.txt
'''
刘备's score is : 215
关羽's score is : 205
张飞's score is : 376
诸葛亮's score is : 100
曹操's score is : 0
'''