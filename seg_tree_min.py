from math import ceil,log2


def make_Tree(arr,l,r,ind,mi):

    if l==r:
        mi[ind]=l
        return l
    
    mid=(l+r)//2

    left=make_Tree(arr,l,mid,2*ind+1,mi)
    right=make_Tree(arr,mid+1,r,2*ind+2,mi)
    if arr[left]<arr[right]:
        mi[ind]= left
    else :
        mi[ind]= right
    return mi[ind]

def get_Min(arr,l,r,s,t,ind,mi):
    if s<=l and t>=r:
        return mi[ind]
    
    if s>r or t<l:
        return -1
    
    mid = (l+r)//2

    left=get_Min(arr,l,mid,s,t,2*ind+1,mi)
    right=get_Min(arr,mid+1,r,s,t,2*ind+2,mi)
    if right==-1:
        return left
    if left==-1 :
        return right
    return left if arr[left]<arr[right] else right
    

arr=[2,5,1,4,9,3]
temp=int(ceil(log2(len(arr))))
mi=[0]*(2*2**temp-1)
make_Tree(arr,0,len(arr)-1,0,mi)
print(mi)
print(get_Min(arr,0,len(arr)-1,0,1,0,mi))