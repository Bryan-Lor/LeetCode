class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window technique: You have two pointers left (l) and right(r)
        # In this case we will slide the right pointer by one, and set the left pointer
        # to it's smallest found value. Then we can calculate the profit and return the max
        # profit via a simple check. Code runs in O(n) time and O(1) space.
        maxP, l  = 0, 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]: 
                prices[l] =  prices[r]
            else:
                profit = prices[r]  - prices[l]
                if profit > maxP:
                    maxP = profit
        return maxP