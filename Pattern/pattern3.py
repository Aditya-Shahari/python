
for x in range(5):
    num = 5 - x
    for y in range(x):
        print(" ", end = " ")
    for z in range((num * 2) - 1):
        if(z < (5 - x - 1)):
            print(num, end=" ")
            num -= 1
        else:
            print(num, end=" ")
            num += 1
    print()