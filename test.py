def solution(A, F, M):
    # write your code in Python 3.6
    sums = (len(A)+F)*M-sum(A)

    s=set()
    def solve(val,i):
        if i>F:
            return False,[]
        if (val,i) in s:
            return False,[]
        for j in range(6,0,-1):
            if val-j>0:
                flg,out=solve(val-j,i+1)
                if flg:
                    return True,[j]+out
                if not flg:
                    s.add((val,j))
            elif val-j==0 and i==F:
                return True,[j]
                
        s.add((val,i))
        return False,[]
    flag,output=solve(sums,1)
    return output if flag else [0]

print(solution([1, 5, 6], 4, 3))