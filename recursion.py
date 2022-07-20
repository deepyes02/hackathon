def main():
    total_cases = int(input().strip())
    if(total_cases < 1 or total_cases > 100):
        return
    arr = []
    counter = 0
    
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

    def my_recurse(total_cases, cntr=0):
        individual_case = int(input().strip())
        # Exit if test cases are not grater than 0 or less than 101
        if(not individual_case > 0 or not individual_case <= 100):
            return
        arr.append(list(map(int, input().rstrip().split())))
        if(not len(arr[cntr]) == individual_case):
            return
        if (total_cases == 1):
            print(*returnValuesFromArray(arr))
            return
        return my_recurse(total_cases - 1, cntr+1)

    my_recurse(total_cases)


main()
