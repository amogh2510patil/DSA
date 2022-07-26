def maxPoints(points) :
    m = len(points)
    n = len(points[0])
    v_max = [0] * n
    
    for r in range(m):
        p = points[r]

        for c in range(n):
            v_max[c] += p[c]
        print(v_max)
        # left to right
        for cl in range(n - 1):
            cr = cl + 1
            v_max[cr] = max(v_max[cl] - 1, v_max[cr])

        # right to left
        for cr in range(n - 1):
            cr = n - 1 - cr
            cl = cr - 1
            v_max[cl] = max(v_max[cr] - 1, v_max[cl])
    
    return max(v_max)
        
arr=[[1,2,3],[1,5,1],[3,1,1]]
print(maxPoints(arr))