import sys
from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_n = len(grid) - 2
        maxLocal = []
        
        for m in range(0,max_n):
            for n in range(0,max_n):
                maxLocal.append((m,n))
        
        dic = {}
        for i in maxLocal:
            dic[i] = []
            
            for j in range(i[0], i[0]+3):
                for k in range(i[1], i[1]+3):
                    dic[i].append((j,k))
        
        res = []
        for m in dic.values():
            ma = 0
            for n in m:
                ma = max(ma, grid[n[0]][n[1]])
            res.append(ma)
            
        res = [res[i:i + max_n] for i in range(0, len(res), max_n)]


        return res

if __name__ == "__main__":
    solution = Solution()
    result = solution.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
    print(result)