class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            px = [0 for _ in range(len(nums))]
            sx = [0 for _ in range(len(nums))]
            
            
            for k, _ in enumerate(nums):
                if k == 0:
                    px[k] = 1 
                else:
                    px[k] = px[k-1] * nums[k-1]
            
            for k,v in enumerate(range(len(nums), 0, -1)):
                if k == 0:
                    sx[k] = 1
                else:
                    sx[k] = sx[k-1] * nums[v]

            sx.reverse()
            
            res = []
            for i in range(len(nums)):
                res.append(px[i] * sx[i])
                
            return res
            

if __name__ == "__main__":
    solution = Solution()
    result = solution.productExceptSelf([1,2,3,4])
    print(result)