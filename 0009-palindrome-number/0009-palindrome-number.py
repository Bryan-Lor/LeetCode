class Solution:
    def isPalindrome(self, x: int) -> bool:
        # O(n) solution where you convert x into a string and compare if it is equal to its
        # reversed sequence. Then simply return its bool value respectively.
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False