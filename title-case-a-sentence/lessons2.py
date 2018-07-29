sentence = "HERE IS MY HANDLE HERE IS MY SPOUT"

def capitalizeFirstLetter(supersentence):
    wordsArray = sentence.split()
    finalCapitalizedLetter = []
    for index, word in enumerate(wordsArray):
        finalCapitalizedLetter.append(word.capitalize())
    return " ".join(finalCapitalizedLetter)

print (capitalizeFirstLetter(sentence))
