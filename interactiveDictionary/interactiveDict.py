from PyDictionary import PyDictionary

def word_meaning(word):
    dictionary = PyDictionary()
    return dictionary.meaning(word)

def word_synonym(word):
    dictionary = PyDictionary()
    return dictionary.synonym(word)

def word_antonym(word):
    dictionary = PyDictionary()
    return dictionary.antonym(word)

word = input("Enter the word:")
print("This word will return with meaning, synonym, antonynm")
print("Meaning :", word_meaning(word))
print("Synonym :", word_synonym(word))
print("Antonym :", word_antonym(word))

#data = json.load(open("Utils/src/interactiveDictionary/data.json", "r"))
# def translate(dictionary):
#      #dictionary = dictionary
#      if word in dictionary:
#          return dictionary.meaning(word)
#      else:
#          return "Word doesn't exist. Please check the word"

# print(translate(dictionary))