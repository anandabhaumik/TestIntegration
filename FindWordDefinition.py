# This program will accept any word from the user and search its corresponding meaning from a source file in JSON format

# import library to load Json files
import json
# import library to determine the nearest match of a word being searched
from difflib import get_close_matches

sourceDataFile = json.load(open("definitionList.json"))


def searchDefinition(wordToSearch):
    word = wordToSearch.lower()
    if word in sourceDataFile:
        return sourceDataFile[word]
    elif len(get_close_matches(word, sourceDataFile.keys())) > 0:
        yn = input(
            "Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, sourceDataFile.keys())[0])
        if yn == "Y":
            return sourceDataFile[get_close_matches(word, sourceDataFile.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


wordInput = input("Enter word: ")

resultDefinition = searchDefinition(wordInput)
if type(resultDefinition) == list:
    for item in resultDefinition:
        print(item)
else:
    print(resultDefinition)
