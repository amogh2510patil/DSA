def Quicksort(arr,start,end):
    pivotele = arr[start]
    pivot = start
    ending = end

    if end >= len(arr) or start <0:
        return arr
    while start < end:

        while arr[start] <= pivotele and start < ending:
            start += 1

        while arr[end] >= pivotele and end > pivot:
            end -= 1

        if start < end:
            arr[start],arr[end] = arr[end],arr[start]
    
    if pivot != end:
        arr[pivot],arr[end] = arr[end],arr[pivot]
        arr = Quicksort(arr,pivot,end-1)
    if end != ending:
        arr = Quicksort(arr,end+1,ending)
    return arr

arr = [9,8,7,9,6,5,4]
print(Quicksort(arr,0,len(arr)-1))    
