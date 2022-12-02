class Solution(object):
    # O(n) solution where you iteratively go through and count the steps similar to fibinacci number
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step1 = step2 = 1
        for i in range(n-1):
            temp = step1 + step2
            step2 = step1
            step1 = temp
        return step1
