def main():
    total_cases = int(input().strip())
    # N (1 <= N <= 100),
    if (total_cases < 1 or total_cases > 100):
        return
    # total_cases = 2
    arr = []
    i = 1
    while i <= total_cases:
        n = int(input().strip())
        # r X (0 < X <= 100),
        if(n < 0 or n > 100):
            return
        arr.append(list(map(int, input().rstrip().split())))
        if(len(arr[i-1]) != n):
            return
        i += 1
    return arr
main()
print("End of code")
