# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
#
# Find the maximum profit you can achieve. You may complete at most k transactions.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
#  
# Example 1:
#
#
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
#
#
# Example 2:
#
#
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#
#
#  
# Constraints:
#
#
# 	0 <= k <= 100
# 	0 <= prices.length <= 1000
# 	0 <= prices[i] <= 1000
#
#


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or len(prices) < 1:
            return 0
        dp = []
        # Can't understood this logic but i copy and paste in this youtube for solving Time Limit Exceeded Problem
        # https://www.youtube.com/watch?v=6928FkPhGUA
        if 2 * k > n:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i -1]:
                    res += prices[i] - prices[i - 1]
            return res;
        # 0 Buy or Skip
        # 1 Sell or Skip
        # 2 SKip or Buy
        for i in range(2*k):
            if i % 2 == 0:
                dp.append(-sys.maxsize -1)
            else:
                dp.append(0)
        for j, price in enumerate(prices):
            for i in range(len(dp)):
                if i == 0:
                    # Buy or Skip
                    dp[i] = max(dp[i], price * -1)
                elif i % 2 == 0:
                    # Buy or Skip
                    dp[i] = max(dp[i], dp[i -1] - price)
                else:
                    # Sell or Skip
                    dp[i] = max(dp[i], dp[i -1] + price)
        print(dp)
        return dp[-1]
