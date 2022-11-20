# Write a program which accepts a string from the user which contains characters from ‘b’ to ‘y’.

userString = input("Enter String: ")

for x in userString:
    if x > "b" and x <"y":
        print(x, end='')
    else:
        print(end= ' ')