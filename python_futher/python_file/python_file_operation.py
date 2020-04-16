fpin = open("scores.txt", encoding='utf-8')  # open file encoding in 'utf-8'
lines = fpin.readlines()
fpin.close()
print(lines)

results = []

for line in lines[:]:
    list1 = line.split()
    print(list1)
    sum = 0
    for score in list1[1:]:
        sum += int(score)
    result = ("%s's score is : %d\n" % (list1[0], sum))
    results.append(result)

print('results:',results)

# write results into results.txt
fpout = open("result.txt", "w", encoding='utf-8')
fpout.writelines(results)
fpout.close()
