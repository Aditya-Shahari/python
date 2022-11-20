
def concatenate(fun):
    def inner(*var):
        ret = fun(*var)
        ans = ""
        for x in ret:
            ans = ans + x
        return ans
    return inner


def isAnagram(fun):
    def inner(*var):
        ret = fun(*var)
        ret[0].lower()
        ret[1].lower()
        count = 0
        for x in ret[0]:
            for y in ret[1]:
                if x == y:
                    count += 1
                    break
        if count == len(ret[0]) and count == len(ret[1]):
            return ret[0], ret[1]
        else:
            print("String is not anagram")
            return " ", " "
    return inner


@concatenate
@isAnagram
def printStr(str1, str2):
    return str1, str2


print(printStr("shashi", "shish"))


