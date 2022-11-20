num = 5
rows = 5
flag = 0
for x in range (rows):
    temp = num
    for y in range (rows - x):
        print("  ", end = " ")

    for z in range (x + 1):
        if(flag == 0):
            print(temp, end=" ")
            temp += num - 2
            flag = 1
        if(flag):
            print(temp, end=" ")
            temp += num

    print(" ")
    flag = 0
    num+=1
