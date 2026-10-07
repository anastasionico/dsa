import collections
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        d = collections.deque()
        res = []
        for r in range(len(nums)):
            while d and nums[r] > nums[d[-1]]:
                d.pop()
            d.append(r)

            if r - k == d[0]:
                d.popleft()
            if (r + 1) >= k:
                res.append(nums[d[0]])
            
            
        return res



                
if __name__ == "__main__":
    solution = Solution()
    result = solution.maxSlidingWindow([1,-1], 1)
    print(result)