sentence = "sHoRt AnD sToUt"

def capitalizedFirstLetter(supersentence):
    wordsArray = sentence.split()
    PustaTablica = []
    for index, words in enumerate(wordsArray):
        PustaTablica.append(words.capitalize())
    return " ".join(PustaTablica)

print (capitalizedFirstLetter(sentence))