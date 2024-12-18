'''

Excercise in the section 3

This project involves creating a program that takes a sentence as input and counts the number of words in that sentence. 
The program will also identify the longest word in the sentence.

/------------------------------------------------------------------------------------------/

My take in this one it is split the sentence by all puntuaction and whitespaces and then search all the words that are the 
longest since it is possible to multiple words hace the same lenght in one sentence.

'''

import re

sentence = str(input("Type a a word or a phrase to count the upper and lowercase letters : "))

words =  words = re.findall(r'\b\w+\b', sentence) #Split the sentence by whitespaces and punctuaction

'''
 (r'\b\w+\b') it is a regular expresion to find all white spaces or puntuaction in the sentence

hW = re.findall(r'\b\w+\b', "Hello, world!")
hW ==> ['Hello' , 'world']
'''

wordsLen = len(words) #number of words in the sentence
longestWord = []
maxLen = 0
for w in words:
    if len(w) > maxLen:
        maxLen = len(w)
        longestWord = [w]
    elif len(w) == maxLen:
        longestWord.append(w) 
    

print(f"The number of words in the sentence is: {wordsLen}")

if len(longestWord) == 1:
    print(f"The longests word in the sentence is: {longestWord} with {maxLen} characters")
else:
    print(f"The longests words in the sentence are: {longestWord} with {maxLen} characters")