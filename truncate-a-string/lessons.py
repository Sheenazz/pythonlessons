def theLongestString(passedSentence, length):
    if len(passedSentence) > length:
        return passedSentence[:length] + '...'
    else:
        return passedSentence


sentence = "A-tisket a-tasket A green and yellow basket"

print(theLongestString(sentence, 12))
