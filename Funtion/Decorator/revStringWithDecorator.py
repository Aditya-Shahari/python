
def reverse(fun):
    def inner(x):
        str = fun(x)
        str1 = str[-1: :-1]
        return str1
    return inner


@reverse
def printStr(str):
    return str


print(printStr("Aditya"))