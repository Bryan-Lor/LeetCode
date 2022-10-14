class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step1 = step2 = 1
        for i in range(n-2, -1, -1):
            fibNum = step1 + step2
            step2 = step1
            step1 = fibNum
        return step1