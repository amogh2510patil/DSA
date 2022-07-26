
def segment_trees(arr,l,r,ind,sum):
    if l==r :
        sum[ind]=arr[l]
        return sum[ind]
    mid=(r+l)//2

    left=segment_trees(arr,l,mid,2*ind+1,sum)
    right=segment_trees(arr,mid+1,r,2*ind+2,sum)
    sum[ind]= left+right
    return sum[ind]

def sums(sum,l,r,s,t,ind):
    if s<=l and r<=t:
        return sum[ind]
    
    if l>t or r<s:
        return 0
    
    mid=(r+l)//2

    return sums(sum,l,mid,s,t,2*ind+1)+sums(sum,mid+1,r,s,t,2*ind+2)

arr=[1, 3, 5, 7, 9, 11]
sum=[0]*15
segment_trees(arr,0,len(arr)-1,0,sum)
print(sum)

print(sums(sum,0,len(arr)-1,1,3,0))

