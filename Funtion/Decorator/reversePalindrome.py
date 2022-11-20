
def palindrome(fun):
    def inner(x):
        rev = fun(x)
        if rev == x:
            return print("Palindrome")
        else:
            return print("Not palindrome")
    return inner


def reverse(fun):
    def inner(x):
        num = fun(x)
        ans = 0
        while num > 0:
            rem = num % 10
            ans = ans * 10 + rem
            num = num // 10
        return ans
    return inner


@palindrome
@reverse
def printNum(x):
    return x


printNum(1)


