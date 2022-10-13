class Solution(object):    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def assignUniqueLetters(s):
            uniqueLetters = []
            numericalLetters = []
            for i in range(0, len(s)):
                if s[i] not in uniqueLetters:
                    uniqueLetters.append(s[i])
                if s[i] in uniqueLetters:
                    numericalLetters.append(uniqueLetters.index(s[i]))
            return numericalLetters
        
        if assignUniqueLetters(s) == assignUniqueLetters(t):
            return True
        else:
            return False
    