class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_f = [0] * 26
        s2_f = [0] * 26
        
        for c in range(len(s1)):
            s1_f[ord(s1[c]) - ord('a')] += 1 
            s2_f[ord(s2[c]) - ord('a')] += 1 
        
        if s1_f == s2_f:
            return True
        
        l = 0
        r = len(s1)

        while r < len(s2):
            s2_f[ord(s2[r]) - ord('a')] += 1 
            s2_f[ord(s2[l]) - ord('a')] -= 1 

            l+=1
            r+=1
            
            if s1_f == s2_f:
                return True

        return False                return True



        
        return False
            

                
if __name__ == "__main__":
    solution = Solution()
    result = solution.checkInclusion('ab', 'eidbaooo')
    print(result)