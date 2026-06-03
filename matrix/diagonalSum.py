class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag_sum = 0 # initialize diagonal sum as 0 
        antidiag_sum = 0 # initialize antidiagonal diagonal sum as 0 
        mat_len = len(mat)
        
        for c in range(0,len(mat)): # go from 0 to 2
            diag_sum += mat[c][c] # c is 0, 1, 2; mat[0][0], mat[1][1],mat[2][2] 
        
        
        r = 0
        c = mat_len -1 # 2

        while r < mat_len:
            # r = 0 c = 2
            antidiag_sum += mat[r][c]
            r += 1
            c -= 1

        middle=0
        # remove middle if matrix in odd (cell 11 of 22 )
        if mat_len %2 != 0:
            middle = mat_len//2
            antidiag_sum -= mat[middle][middle]

        return diag_sum + antidiag_sum

if __name__ == "__main__":
    solution = Solution()
    result = solution.diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
    print(result)