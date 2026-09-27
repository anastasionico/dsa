class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for t in range(len(temperatures)):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                diff = temperatures[t] - temperatures[stack[-1]]
                top_of_stack = stack.pop()
                res[top_of_stack] = diff
                
            
            stack.append(t)
            print(res, stack)
        return res
        
            

if __name__ == "__main__":
    solution = Solution()
    result = solution.dailyTemperatures([1,2,3,4])
    print(result)