class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(n) Solution where you iterate through the list to determine the minimum two steps at a time.
        # Then you store it back into the list (to save memory) and then returning it at the very end
        n = len(cost)
        for i in range(2, n):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[n-1], cost[n-2])