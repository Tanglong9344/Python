# break
while True:
    x = input("Input a string,'q'for quit: ")
    if x == 'q':
        break    # run out of loop
    print(x)

# continue
while False:
    try:
        x = int(input("input a number,>100 for quit: "))
    except Exception as e:
        print('input error:',e)
        continue
    if x <= 100:
        print(x)
        continue  # continue the next loop
    if x > 100:
        break     # run out of loop
