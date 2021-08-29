import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {} instead? Type 'Y' for yes and 'N' for no: ".format(get_close_matches(word, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Such a word does not exist in the dictionary. Please re-check the entered word."
        else:
            return "We didn't understand your entry."
    else:
        return "Such a word does not exist in the dictionary. Please re-check the entered word."
    
word = input("Enter word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)