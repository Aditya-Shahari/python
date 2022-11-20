
print("start")

def reverse(fun):
    print("inside fun")
    def inner(*args):
        print("inside inner1")
        retTup = fun(*args)
        return retTup[-1: :-1]
    return inner

def concat(gun):
    print("inside gun")
    def inner(*args):
        print("inside inner2")
        retTup = gun(*args)
        str2 = " "
        for x in retTup:
            str2 = str2 + x
        return str2
    return inner

print("above decorator")


@reverse
@concat
def printStr(str1, str2):
    print("inside printStr")
    return str1, str2

print("above final print")
print(printStr("Aditya", "Shahari"))

print("end")