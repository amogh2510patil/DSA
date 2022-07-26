def InsertionSort(arr):
    for i in range(1,len(arr)):
        element = arr[i]
        j = i-1
        while j>=0 :
            if arr[j] > element:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = element
    return arr   

arr = [9,4,6,3,7,5,4,0]
print(InsertionSort(arr))