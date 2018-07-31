def theLongestString(passedSentence, length):
    wordsArray = passedSentence.split()
    if len(passedSentence) >= 8:
        return wordsArray[0]

sentence = "A-tisket a-tasket A green and yellow basket"

print(theLongestString(sentence, 8),"...")
