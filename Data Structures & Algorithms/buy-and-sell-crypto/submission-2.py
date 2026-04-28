class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        prof = 0
        while left < len(prices) and right < len(prices):
            while right < len(prices) and prices[right] > prices[left]:
                prof = max(prof, prices[right] - prices[left])
                right += 1
            left = right
            right += 1
        return prof