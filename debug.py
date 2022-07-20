arr = [[1, -1, 2], [-33, 3, -23, 4], [5, -34, -99, 6], [2,-2,-2,-2,3]]


def sumofarray(anotherArr, summ=0, length=0):
    if(length == len(anotherArr)):
        return summ
    else:
        summ = summ + anotherArr[length]
        return sumofarray(anotherArr, summ, length+1)


def squareofpositives(newArr, x, anotherArr):
    # global anotherArr
    if(x == len(newArr)):
        return sumofarray(anotherArr)
    else:
        if(newArr[x] > 0):
            anotherArr.append(newArr[x]**2)
        return squareofpositives(newArr, x+1, anotherArr)

def false_if_negative(arr, y, newArr):
    # return function if any input is greater than
    if (y == len(arr)):
        return squareofpositives(newArr, 0, [])
    else:
        if(arr[y] > 100 or arr[y] < -100):
            return
        newArr.append(arr[y])
        return false_if_negative(arr, y+1, newArr)

def returnValuesFromArray(arr):
    # global resultArr
    counter = 0
    appendArr = []
    while(counter < len(arr)):
        appendArr.append(false_if_negative(arr[counter], 0, []))
        counter = counter + 1
    return appendArr

print(returnValuesFromArray(arr))
