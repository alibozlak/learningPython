def getCube(intNumber) : 
    return intNumber * intNumber * intNumber

def getSquare(intNumber) : 
    return intNumber * intNumber

def doSometingInGivenArray(array, function) :
    resultArray = []
    for number in array : 
        resultArray.append(function(number))
    print(resultArray)


array = [1,2,3,4,5,6,7,8,9,10]
doSometingInGivenArray(array, getCube)      #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
doSometingInGivenArray(array, getSquare)    #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]