class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        f = 0
        s = 0

        for i in nums:
            if i > s:                
                if i > f:
                    s = f
                    f = i
                else:
                    s = i

        return nums.index(f) if (f/2) >= s else -1        