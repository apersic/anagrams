import sys

#Read the arguments.
fileName = sys.argv[1]
w = sys.argv[2]

#Opening and reading the file.
file = open(fileName, "r")
list = file.readlines()

#Function that sorts the letters in a word.
def CleanString(item):
    cleanedString = "".join(sorted(item))
    return cleanedString

#Iterating through the words and comparing them to the argument word.
count = 0
for word in list:
    if CleanString(word.strip()) == CleanString(w.strip()):
        count += 1
print("Result: {}".format(count))

#Closing the file.
file.close()