class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Simply split the string by white space and then get the length of last word
        x = s.split()
        return len(x[len(x) - 1])