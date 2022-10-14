class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
#         # Time: O(n), Space: O(1)
#         step1 = cost[0]
#         step2 = cost[1]
#         cost.append(0)
        
#         for i in range(2, len(cost)):
#             c = min(step1, step2) + cost[i]
#             print(step1,step2,c)
#             step1 = step2
#             step2 = c
#         return c

        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
            #print(i,cost[i])
            #print(cost)
        n = len(cost)
        return min(cost[n-1], cost[n-2])