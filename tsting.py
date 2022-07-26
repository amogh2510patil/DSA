from typing import Tuple


class Solution:
    def findSum(lst,target):
        out = []
        flag = False
        print(lst)
        print(target)
        for i,ele in enumerate(lst):
            if ele < target:
                flag2,l = Solution.findSum(lst[i:],target-ele) 
                print(l,lst,target)
                if flag2:
                    flag = flag2
                    for t in l:
                        t.insert(0,ele)
                    out.extend(l)
            elif ele > target:
                break
            else:
                out.append([ele])
                flag = True
                break
        print(lst,target,flag,out)
        print()
        return flag,out
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        return(Solution.findSum(candidates,target))


obj = Solution()
print(obj.combinationSum([2,3,6,7],7))
