from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit, min_value = 0, float('inf')
        for price in prices:
            min_value = min(min_value, price)
            profit = max(profit, price - min_value)
        return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices), 5)

    prices = [7, 6, 4, 3, 1]
    print(sol.maxProfit(prices), 0)
