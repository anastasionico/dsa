class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for k,i in enumerate(nums):
            diff = target - i
            
            if diff in seen:
                return [seen.get(diff), k]
            

            seen[i] = k
            

if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSum([2,7,11,15], 9)
    print(result)