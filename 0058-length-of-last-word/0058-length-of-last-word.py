class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Simply split the string by white space and then get the length of last element/word
        x = s.split()
        return len(x[len(x) - 1])