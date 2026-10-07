from collections import Counter
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        want = Counter(t)
        have = {}
        
        lenght, l_res = inf, -1
        matched = 0
        
        l = 0
        for r, c in enumerate(s):
            # add the s letters to have
            have[c] = 1 + have.get(c, 0)
                
            # if the letter in have is smaller or equal to the letter in want increase the matched counter
            if have[c] <= want[c]:
                matched +=1

            # while the lenght of t is the same of the matched value move l to the left
            while matched == len(t):
                # calculate the new l
                if r - l + 1 < lenght:
                    lenght = r - l + 1
                    l_res= l
                
                # if l is in want and have have less or equal element of want decrease the counter
                if s[l] in want and  have[s[l]] <= want[s[l]]:
                        matched -= 1
                # move the l pointer
                have[s[l]] -= 1
                l += 1
                
        return '' if l_res == -1 else s[l_res:l_res+lenght]


                
if __name__ == "__main__":
    solution = Solution()
    result = solution.minWindow('AABC', 'ABC')
    print(result)