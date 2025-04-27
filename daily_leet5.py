class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

solution = Solution()
print("Test 1 - Expected: 5", solution.maxProfit([7, 1, 5, 3, 6, 4]))
print("Test 2 - Expected: 0", solution.maxProfit([7, 6, 4, 3, 1]))
print("Test 3 - Expected: 3", solution.maxProfit([2, 4 ,1, 5]))
