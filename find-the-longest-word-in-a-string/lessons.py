def findingLongestWord(words):
  wordsArray = words.split(" ")
  max = len(words[0])
  for word in wordsArray:
    if max <= len(word):
      maxWord = word
      max = len(word)
  return maxWord



print("longest", findingLongestWord("Matiaaaaa jest super"))
