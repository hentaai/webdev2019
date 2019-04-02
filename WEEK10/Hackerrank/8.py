if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in arr:
        max1 = -101
        if arr[i]>max1:
            max = arr[i] 
    for i in arr:
        max2 = -101
        if arr[i]>max2 and arr[i]!=max1:
            max2 = arr[i]
    print(max2)
