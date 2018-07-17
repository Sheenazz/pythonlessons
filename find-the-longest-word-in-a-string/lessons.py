words = "The quick brown fox jumped over the lazy dog"

array = words.split(" ")
longest = max(array, key = len)

print(longest)
