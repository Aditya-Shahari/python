# Write a program which accepts sentences from the user
# and print a number of small letters, capital letters and digits from that sentence

userString = input("Enter String: ")

small = 0
capital = 0
digits = 0

for x in userString:
    if x >= "A"  and x <= "Z":
        capital+= 1
    elif x >= "a" and x <= "z":
        small+=1
    elif x >= "0" and x <= "9":
        digits += 1

print("Small:", small)
print("Capital:", capital)
print("Digits:", digits)