#old data
'''
#-- scores.txt
刘备 23 35 44 47 66
关羽 60 77 68
张飞 97 99 89 91
诸葛亮 100
曹操 
'''
# data dealing
fpin = open("scores.txt",encoding='utf-8')#open file encoding in 'utf-8'
lines = fpin.readlines()
fpin.close()
print (lines)

results = []

for line in lines[ : ]:
    # print("line: " + line)
    l = line.split()
    print (l)
    sum = 0
    for score in l[1 : ]:
        sum += int(score)
    result = ("%s's score is : %d\n" %(l[0], sum))

#get every one's score
    results.append(result)

#write results into results.txt
fpout = open("result.txt", "w", encoding='utf-8')
fpout.writelines(results)
fpout.close()