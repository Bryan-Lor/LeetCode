class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        foundLetters = 0
        for char in s:
            for letter in t:
                if char == letter:
                    foundLetters += 1
                    t = t[t.index(letter)+1:len(t)]
                    break
        if foundLetters == len(s):
            return True
        else:
            return False