A=[84,80,27]
def solve(i,stk=[]):
    if i>=len(A):
        return len(stk)
    left=0
    right=0
    if not stk or A[i]>stk[-1]:
        stk.append(A[i])
        left=solve(i+1,stk.copy())
        stk.pop()
    else:
        left=solve(i+1,stk.copy())
        while stk and A[i]<stk[-1]:
            stk.pop()
        stk.append(A[i])
        right=solve(i+1,stk.copy())
        stk.pop()
    return max(left,right)

print(solve(0))
