arr = [1, 2, -3, -94, -5, -6]
newArr = []
anotherArr = []

def sumofarray(arr, sum=0, length=0):
    if(length == len(arr)):
        return sum
    else:
       sum = sum + arr[length]
       length = length + 1
       return sumofarray(arr,sum,length)

def squareofpositives(arr, x=0):
    global anotherArr
    if(x == len(arr)):
        return sumofarray(anotherArr);
    else:
        if(arr[x] > 0):
            anotherArr.append(arr[x]**2)
        x = x + 1
        return squareofpositives(arr, x)

def false_if_negative(arr, y=0):
    global newArr
    if (y == len(arr)):
    	return squareofpositives(newArr)
    else:
        if(arr[y] > 100 or arr[y] < -100):
            return
        newArr.append(arr[y])
        y = y + 1
        return false_if_negative(arr, y)

print(false_if_negative(arr))