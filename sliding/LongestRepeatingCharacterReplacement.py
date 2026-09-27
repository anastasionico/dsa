class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lon = 0
        seen = {}

        l = 0
        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)

            
            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1

            lon = max(lon, (r - l + 1))
                


        return lon
            

                
if __name__ == "__main__":
    solution = Solution()
    result = solution.characterReplacement('ABAA', 0)
    print(result)