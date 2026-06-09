from collections import Counter

class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
        cs = Counter(s)
        ct = Counter(t)
        return True if cs == ct else False

if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s,t)
    print(result)