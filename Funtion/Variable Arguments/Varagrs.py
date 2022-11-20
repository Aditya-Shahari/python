# def sum (a, *b):
#
#     print(a,b)
#     print(type(b))   #tuple
#
# sum(20, 1)
# sum(20)
# sum(20, 1, 3 ,4)


def addVar(*args):
    sum = 0
    for x in args:
        sum = sum + x

    return sum

x = int(input("Enter number: "))
y = int(input("Enter number: "))
z = int(input("Enter number: "))
print(addVar(x , y, z))