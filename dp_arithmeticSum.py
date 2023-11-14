def nSum(i: int) -> int:
    arr = [0 for j in range(i+1)]

    arr[0] = 0
    for j in range(1,i+1):
        arr[j] = arr[j-1] + j
    
    return arr[len(arr)-1]


a = nSum(5)
print(a)