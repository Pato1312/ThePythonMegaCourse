"""
* The excercise consist in recive multiple sentences untill "/end" is input
* Then the program will format them capitalizing the first letter and adding a dot at the end or
a "?" if it is a question
/--------------------------------------------------------------------/
My answer consist in defining a function to formtat the sentences, 
the program will read, format them and add to the list, if "/end" is input the loop will end
and remove it from the list, at the end the full formated list is printed
"""


def sentenceMaker(phrase):
    interrogative = (
        "what",
        "why",
        "when",
        "where",
        "who",
        "whom",
        "which",
        "how",
        "What",
        "Why",
        "When",
        "Where",
        "Who",
        "Whom",
        "Which",
        "How",
    )
    if phrase.startswith(interrogative):
        return "{}?".format(phrase.capitalize())
    else:
        return "{}.".format(phrase.capitalize())


phrase = " "
sentence = []


while phrase != "/end":
    phrase = input("Say something : ")
    sentence.append(sentenceMaker(phrase))

sentence = sentence[:-1]  # remove "\end" from the last item of the list

print(" ".join(sentence))
