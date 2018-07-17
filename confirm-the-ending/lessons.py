str = "Never give up and good luck will find you"

suffix = "you"

wordsArray = str.split(" ")
wordsArrayLength = len(wordsArray)
if wordsArray[wordsArrayLength-1] == suffix:
  print("True")

# print (str.endswith(suffix))