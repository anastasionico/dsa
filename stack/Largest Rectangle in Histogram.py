class Solution:
    def largestRectangleArea(self, heights):
        stack = []              # stores indexes
        maxArea = 0
        # Add a fake 0 at the end to force everything to be popped
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                    
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea
        
if __name__ == "__main__":
    solution = Solution()
    result = solution.largestRectangleArea([2,1,2])
    print(result)