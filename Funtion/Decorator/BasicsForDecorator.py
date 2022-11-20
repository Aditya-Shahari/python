
# print("start")
# def fun():
#     print("Inside fun")
#     def inner():
#
#         return "Inner Func"
#     print(id(inner()))
#     return inner
#
#
# print("above obj")
# retFun = fun()
# print(retFun)
# print("below obj")
# print(retFun())     # reTfun has address of inner hence when you call reTfun() it calls directly inner functions
# print(id(retFun()))

print("start")
def fun():
    print("inside fun")
    def inner1():
        return "Inner1 Func"
    def inner2():
        return "Inner2 Func"

    print("above return")
    return inner1, inner2

print("above obj")
retFun = fun()
print(retFun)
print("below obj")
for x in retFun:
    print(x())
print("end")
