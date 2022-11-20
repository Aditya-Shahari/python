# Write a program which accepts sentences from the user and prints a number of words from that sentence

userString = input("Enter string: ")

x = 0

if userString[0] == " ":
    count = 0
else:
    count = 1

for x in range (len(userString)):
    if userString[x] == " " and userString[x + 1] != " ":
        count += 1
print(count)