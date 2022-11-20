# Write a program which accepts sentences from the user
# and print a number of words of even and odd length from that sentence.

userString = input("Enter string: ")
even = 0
odd = 0
count = 0
y = 0
for x in range(len(userString)):
    while y < len(userString):
        if userString[y] == ' ':
            y += 1
            break
        count += 1
        y += 1
    if count % 2 == 0:
        even += 1
    else:
        odd += 1
    count = 0

print("Odd:", odd)
print("Even:", even)