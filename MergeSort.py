def MergeSort(arr):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    if len(left) > 1:
        left = MergeSort(left)
    
    if len(right) > 1:
        right = MergeSort(right)
    
    array = []

    l = 0 
    r = 0
    while l<len(left) and r < len(right):
        if left[l] < right[r]:
            array.append(left[l])
            l+=1
        else:
            array.append(right[r])
            r+=1
    while l<len(left):
        array.append(left[l])
        l += 1
    while r<len(right):
        array.append(right[r])
        r += 1
    
    return(array)

arr = [1,5,3,2,8,7,4,8,3,2]
print(MergeSort(arr))
