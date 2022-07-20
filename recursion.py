def main():
    total_cases = int(input().strip())
    if(total_cases < 1 or total_cases > 100):
        return
    arr = []
    counter = 0

    def my_recurse(total_cases, cntr=0):
        individual_case = int(input().strip())
        #Exit if test cases are not grater than 0 or less than 101
        if(not individual_case > 0 or not individual_case <= 100):
            return
        arr.append(list(map(int, input().rstrip().split())))
        if(not len(arr[cntr]) == individual_case):
            return
        if (total_cases == 1):
            print(arr)
        return my_recurse(total_cases - 1, cntr+1)

    my_recurse(total_cases)


main()
