class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [[1] for i in range(len(nums))]

        pre = 1
        for n in range(len(nums)):
            res[n] = pre
            pre *= nums[n]

        post = 1
        for n in range(len(nums)-1, -1, -1):
            res[n] *= post 
            post *= nums[n]

        return res

            

if __name__ == "__main__":
    solution = Solution()
    result = solution.productExceptSelf([1,2,3,4])
    print(result)