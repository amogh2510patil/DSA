class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def MergeSort(head,end=None):
    
    len = 0
    temp=head
    while temp!=end:
        len+=1
        temp=temp.next

    if len<=1:
        return head

    if len%2==0:
        mid=len//2
    else:
        mid=len//2+1

    midele = head
    for i in range(1,mid+1):
        midele = midele.next
    
    if head.next != midele:
        head=MergeSort(head,midele)
    if midele.next != end:
        midele=MergeSort(midele,end)

    temp1=head
    l=[None]*mid
    i=0
    while temp1!=midele:
        l[i] = temp1.data
        temp1 = temp1.next
        i+=1
    
    r=[None]*(len-mid) 
    j=0
    temp2=midele
    while temp2!=end:
        r[j]=temp2.data
        temp2 = temp2.next
        j+=1
    

    i=0
    j=0
    temp=head
    while i<mid and j<len-mid:
        if l[i] > r[j]:
            temp.data=r[j]
            temp=temp.next
            j+=1
        else:
            temp.data=l[i]
            temp=temp.next
            i+=1

    while i<mid:
        temp.data=l[i]
        temp=temp.next
        i+=1
    while j<(len-mid):
        temp.data=r[j]
        temp=temp.next
        j+=1
    return head

head=Node(10)
arr=[3,5, 2, 4, 1]
temp=head
for i,ele in enumerate(arr):
    temp.next=Node(ele)
    temp=temp.next

head=MergeSort(head)
temp=head
while temp:
    print(temp.data)
    temp=temp.next