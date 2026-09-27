class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(len(prices) - 1, -1, -1):

            # Remove prices that cannot be a discount
            while stack and stack[-1] > prices[i]:
                stack.pop()

            # If stack is empty, no discount
            if stack:
                res.append(prices[i] - stack[-1])
            else:
                res.append(prices[i])

            # Current price becomes available
            # as a discount for things further left
            stack.append(prices[i])

        return res[::-1]

                
if __name__ == "__main__":
    solution = Solution()
    result = solution.finalPrices([8,4,6,2,3])
    print(result)