def copiedArray(firstArray, secondArray, toInsertIndex):
    print(firstArray[1:toInsertIndex])
    firstArray[toInsertIndex:toInsertIndex] = secondArray
    return firstArray
    # for index, secondArrayElement in enumerate(secondArray):
    #     firstArray.insert(toInsertIndex+index, secondArrayElement)
    # return firstArray

firstArray = [1, 2, 3]
secondArray = [4, 7, 8]
index = 2   

print(copiedArray(firstArray, secondArray, index))