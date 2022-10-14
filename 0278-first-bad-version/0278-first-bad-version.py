# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Binary Search Algorithm with Left Pointer
        # We will use n as our rightPointer
        # ex:
        #rightPointer = n
        leftPointer = 1
        while leftPointer <= n:
            searchPointer = (n + leftPointer) // 2
            if isBadVersion(searchPointer):
                if isBadVersion(searchPointer - 1):
                    n = searchPointer - 1
                else:
                    return searchPointer
            else:
                leftPointer = searchPointer + 1