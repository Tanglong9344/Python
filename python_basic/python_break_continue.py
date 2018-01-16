# break && continue
# break
while True:
    x = input("Input strings and 'q'for quit: ")
    print(x)
    if x == 'q':
        break    # run out of loop

# continue
while True:
    x = int(input("input numbers and 110 for quit: "))
    if x < 60:
        continue  # continue the next loop
    print(x)
    if x == 110:
        break     # run out of loop
