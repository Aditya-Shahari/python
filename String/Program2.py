# Write a program which accepts a string from the user which contains characters from âbâ to âyâ.

userString = input("Enter String: ")

for x in userString:
    if x > "b" and x <"y":
        print(x, end='')
    else:
        print(end= ' ')