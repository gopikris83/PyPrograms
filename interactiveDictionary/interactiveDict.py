from PyDictionary import PyDictionary
from googletrans import Translator, constants
from pprint import pprint

# Defines the meaning for the given word
def word_meaning(word):
    dictionary = PyDictionary()
    return "The word does not exist. Please check the word" if dictionary.meaning(word) is None else str(', '.join(str(e) for e in dictionary.meaning(word).values()))
    

# Defines the synonym  for the given word
def word_synonym(word):
    dictionary = PyDictionary()
    return "The word does not exist. Please check the word" if dictionary.synonym(word) is None else ', '.join(str(e) for e in dictionary.synonym(word))
    

# Defines the antonym for the given word
def word_antonym(word):
    dictionary = PyDictionary()
    return "The word does not exist. Please check the word" if dictionary.antonym(word) is None else ', '.join(str(e) for e in dictionary.antonym(word))
    

# Translates the word into Swedish
def word_translate(word):
    translator = Translator()
    translation = translator.translate(word, dest='sv')
    # pprint(constants.LANGUAGES)
    return print(f"Translation to Swedish: {translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

word = input("Enter the word:")

print("Entered word will return with meaning, synonym, antonynm")
print("Meaning :", word_meaning(word))
print("Synonym :", word_synonym(word))
print("Antonym :", word_antonym(word))

word_translate(word)
#data = json.load(open("Utils/src/interactiveDictionary/data.json", "r"))
# def translate(dictionary):
#      #dictionary = dictionary
#      if word in dictionary:
#          return dictionary.meaning(word)
#      else:
#          return "Word doesn't exist. Please check the word"

# print(translate(dictionary))