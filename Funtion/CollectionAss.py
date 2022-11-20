def collectionFun(num):
    def prime():
        flag = 0
        c = 2
        while c < num:
            if num % c == 0:
                flag = 1
                break
            c += 1

        if flag == 1:
            print("Not prime")
        else:
            print("Prime")


    def palindrome():
        original = num
        new = 0
        while(original != 0):
            rem = original % 10
            new = new * 10 + rem
            original = original//10

        if num == new:
            print("Palindrome")
        else:
            print("Not palindrome")

    def armstrong():
        org1 = num

        power = 0

        while(org1 != 0):
            rem = org1 % 10
            power += 1
            org1 = org1//10

        org2 = num
        sum = 0
        while(org2 != 0):
            remn = org2 % 10
            sum = sum + remn**power
            org2 = org2//10

        if sum == num:
            print("Armstrong")
        else:
            print("Not armstrong")

    def reverse():
        s = 0
        org = num
        while(org != 0):
            r = org % 10
            s = s * 10 + r
            org = org // 10

        print(s)

    return prime(), palindrome(), armstrong(), reverse()

collectionFun(153)
