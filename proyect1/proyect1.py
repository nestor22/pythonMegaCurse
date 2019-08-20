import json
import difflib
from difflib import get_close_matches

data = json.load(open("/home/salem/Documents/04 universidad/05-python/megacurso/proyect1/076 data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        anser = input("Did you mean %s instead?yes/no\n" % get_close_matches(word, data.keys())[0] )
        if anser == 'yes':
            return data[get_close_matches(word, data.keys())[0]]
        elif anser == 'no':
            return "the word doesn't exist.Please double check."    
        else:
            return "I can't you entry"

    else: 
        return "the word doesn't exist.Please double check."

word = input ("Enter word: ")
output = translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)