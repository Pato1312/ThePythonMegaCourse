"""

Excercise in the chapter 3.14 

This program defines a string, counts how many uppercase and lowercase letters are present, and displays both counts.
"""

# The program read a phrase and with the function strip take off all the spaces
phrase = str(
    input("Type a a word or a phrase to count the upper and lowercase letters : ")
).strip()

countUP = 0
countLow = 0

for i in phrase:
    if i.isupper():
        countUP += 1
    elif i.islower():
        countLow += 1

print("The ammount of uppercase letters is : ", countUP)
print("The ammount of lowercase letters is : ", countLow)
