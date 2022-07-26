def Binary_search(arr,key):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            r = mid-1
        else :
            l = mid+1
    return -1

array = [1,3,5,7,8,56,67,79,90,121,145,233,567]
print(Binary_search(array,120))