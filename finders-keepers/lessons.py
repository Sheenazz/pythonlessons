sentence = "I'm a little tea pot"


def capitalizeFirstLetter(supersentence):
    wordsArray = supersentence.split()
    finalCapitalizedWordsArray = []
    for index, word in enumerate(wordsArray):
        finalCapitalizedWordsArray.append(word.capitalize())
    return " ".join(finalCapitalizedWordsArray)
   

print(capitalizeFirstLetter(sentence))
