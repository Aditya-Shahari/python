
"""x = 10
def fun1():
    y = y + 20
    print(x)
    print(y)

fun1()"""
# Error because of variable referenced before assignment

x = 10
def fun1(y):
    y = y + 20
    print(x)
    print(y)

fun1(20)