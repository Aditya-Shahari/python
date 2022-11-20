print("start")


def mult(fun):
    print("inside fun")

    def magic (x):
        print("inside magic")
        ans = fun(x)
        return ans * x
    print("above return")
    return magic


@mult
def sqr(x):
    print("above return sq")
    return x*x


print("above sqr")
print(sqr(5))

# retFun = sqr(5)
# print(retFun)




