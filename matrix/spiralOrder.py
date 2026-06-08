class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix)-1
        res = []

        while t <= b and l <= r:
            # going right
            for c in range(l, r+1):
                res.append(matrix[t][c])

            t +=1
            
            # # going down
            for row in range(t, b+1):
                res.append(matrix[row][r])
              
            r-=1
            
            # going left
            if t <= b:
                for i in range(r, l-1, -1):
                    res.append(matrix[b][i])
                        
                b -=1

            # #going up
            if l <= r:
                for i in range(b, t-1, -1):
                    res.append(matrix[i][l])
                
                l +=1            

        return res

if __name__ == "__main__":
    solution = Solution()
    result = solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    print(result)