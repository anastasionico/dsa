class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        multiplied = []
        m = pow(10, len(digits)-1)
        
        for i in digits:
            multiplied.append(int(i * m))     
            m //= 10
        
        sum = 1
        for d in multiplied:    
            sum += d
        sum = [int(x) for x in str(sum)]

        return sum
