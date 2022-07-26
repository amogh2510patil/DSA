from math import ceil,log2
def segment_Tree(arr,out,l,r,ind):
    if l==r:
        out[ind]=arr[l]
        return arr[l]
    
    mid=(l+r)//2

    out[ind]=max(segment_Tree(arr,out,l,mid,2*ind+1),segment_Tree(arr,out,mid+1,r,2*ind+2))
    return out[ind]

def findEle(out,l,r,s,t,ind):

    if t<l or s>r:
        return -1e5
    
    if s<=l and t>=r:
        return out[ind]
    mid=(l+r)//2
    return max(findEle(out,l,mid,s,t,2*ind+1),findEle(out,mid+1,r,s,t,2*ind+2))

arr=[1, 3, 5, 7, 9, 11]
temp= int(ceil(log2(len(arr))))
out=[0]*(2*2**temp-1)
segment_Tree(arr,out,0,len(arr)-1,0)
print(findEle(out,0,len(arr)-1,2,5,0))
