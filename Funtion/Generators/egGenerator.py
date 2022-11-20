

def fun():
    yield 10
    yield 20
    yield 40

genobj = fun()
print(type(genobj))

for x in fun():
    print(x)