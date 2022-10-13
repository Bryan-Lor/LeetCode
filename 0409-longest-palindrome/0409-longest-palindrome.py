class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        setValues = set(s)
        for c in setValues:
            if s.count(c) > 1 and s.count(c) % 2 == 0:
                temp.append(s.count(c))
            else:
                temp.append(s.count(c)-1)
        if sum(temp) == len(s):
            return sum(temp)
        else:
            return sum(temp) + 1
                
                