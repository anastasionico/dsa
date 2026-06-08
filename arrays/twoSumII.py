class Solution:
    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        l = 0

        for k,v in enumerate(numbers):
            diff = target - v

            if diff in seen:
                return [seen[diff]+1, k+1]

            seen[v] = k

if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSumII([2,7,11,15], 9)
    print(result)