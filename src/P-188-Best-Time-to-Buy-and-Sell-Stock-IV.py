'''
P-188 - Best Time to Buy and Sell Stock IV

Say you have an array for which theithelement is the price of a given
stock on dayi. Design an algorithm to find the maximum profit. You may
complete at mostktransactions. Note:You may not engage in multiple
transactions at the same time (ie, you must sell the stock before you
buy again). Credits:Special thanks to@Freezenfor adding this problem
and creating all test cases.

Tags: Dynamic Programming
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer

    # DP-based Solution
    # d[i][j] means with i transactions the maximum profit up to j days
    # k is the number of transactions allowed
    # Memory exceeded
    def maxProfit(self, k, p):
        if len(p) < 2:
            return 0
        d = [[0] * len(p) for _ in range(k + 1)]
        for i in range(1, k + 1):
            curr_max = -p[0]
            for j in range(1, len(p)):
                d[i][j] = max(d[i][j - 1], p[j] + curr_max)
                curr_max = max(curr_max, d[i - 1][j] - p[j])
        return d[-1][-1]