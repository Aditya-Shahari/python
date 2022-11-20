# x = 10
# def fun1():
#     # print(x) error treats it as local variable, and it is not defined
#     x = 20
#     print(x)
#
# fun1()
# print(x)

# x = 10
# def fun1():
#     global x
#     x = 20
#     print(x)
#
# fun1()
# print(x)

x = 10
def fun1 ():
    x = 20
    print(x)
    print(globals()['x'])

fun1()

















