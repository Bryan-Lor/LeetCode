class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # O(N^2) Brute Force Solution
        maxNum = ""
        for i in range(len(number)):
            if number[i] == digit:
                newString = number[:i] + number[i+1:]
                if newString > maxNum:
                    maxNum = newString
        return maxNum