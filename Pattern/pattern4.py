
n = 7
for i in range(1, (n*2) + 1):
    if i <= ((n // 2) + 1):
        for j in range(i):
            print("#", end=' ')
    elif i <= 7:
        for j in range((n - i) + 1):
            print("#", end=' ')
    elif i <= ((n * 2) - (n // 2)):
        for j in range(i - n):
            print("#", end=' ')
    elif i <= (n * 2) :
        for j in range(((n*2) + 1 - i)):
            print("#", end=' ')
    print()

