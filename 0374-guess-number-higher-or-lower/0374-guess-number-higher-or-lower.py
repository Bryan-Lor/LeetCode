# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        #print(n)
        while l <= r:
            m = (l+r) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                #print("number picked is higher")
                l = m + 1
            else:
                #print("number picked is lower")
                r = m - 1
            print(m, l, r)
                