def ShellSort(arr,gap):

    for i in range(gap,len(arr)):
       element = arr[i]
       j = i-gap
       while j>=0 and element <arr[j]:
           arr[j+gap] = arr[j]
           j-=gap
       arr[j+gap] = element
    return(arr)

arr = [9,6,3,2,7,4,8,1]
for l in range(len(arr)//2,0,-1):
    print(l)
    arr = ShellSort(arr,l)
    print(arr)

print()
print(arr)
