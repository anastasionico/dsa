class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
    
        
        freq = [[] for i in range(len(nums) + 1)]
        for n, f in count.items():
            freq[f].append(n)
        
        res = []
        for i in range(len(freq)-1, -1 , -1):
            for i in freq[i]:
                res.append(i)
                if len(res) == k:
                    return res
            

if __name__ == "__main__":
    solution = Solution()
    result = solution.topKFrequent([1,1,1,2,2,3], 2)
    print(result)