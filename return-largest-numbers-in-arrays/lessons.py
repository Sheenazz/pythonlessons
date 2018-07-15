numbers = [[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]

arrayOfLargestNumber = []
def findingLargestNumberInArrays(arrayOfArraysOfNumbers):
    for arrayOfNumbers in arrayOfArraysOfNumbers:
      max = arrayOfNumbers[0]
      for number in arrayOfNumbers:
        if number > max:
            max = number
      arrayOfLargestNumber.append(max)

findingLargestNumberInArrays(numbers)

print("Largest found:")
for number in arrayOfLargestNumber:
    print(number)