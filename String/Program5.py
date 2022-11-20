# Write a program which accepts sentences from the user and print a number of white spaces from that sentence.

userString = input("Enter String: ")
count = 0
for x in userString:
    if x == " ":
        count += 1
print(count)