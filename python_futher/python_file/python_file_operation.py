# old data:scores.txt
# data dealing
fpin = open("scores.txt", encoding='utf-8')  # open file encoding in 'utf-8'
lines = fpin.readlines()
fpin.close()
print(lines)

results = []

for line in lines[:]:
    # print("line: " + line)
    list0 = line.split()
    print(list0)
    sum0 = 0
    for score in list0[1:]:
        sum0 += int(score)
    result = ("%s's score is : %d\n" % (list0[0], sum0))

# get every one's score
    results.append(result)

# write results into results.txt
fpout = open("result.txt", "w", encoding='utf-8')
fpout.writelines(results)
fpout.close()
