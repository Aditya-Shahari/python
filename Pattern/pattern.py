num = 1
sum = 0
rows = 3
for x in range (rows):
    for y in range(rows):
        print(num, end = " ")
        if(x==y):
            sum = sum + num
        elif(x+y == 3 - 1):
            sum = sum + num
        num += 1
    print()


print(sum)