char = 65
num = 1
for i in range(2):
    print("* * *")
    for j in range(3):
        print(chr(char), end=" ")
        char += 1
    print()
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()