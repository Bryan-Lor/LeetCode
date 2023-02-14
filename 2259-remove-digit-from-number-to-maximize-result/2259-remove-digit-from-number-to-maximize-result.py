class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # O(N^3) Brute Force Solution
        maxNum = ""
        for i in range(len(number)):
            if number[i] == digit:
                leftString = number[:i]
                rightString = number[i+1::]
                if leftString + rightString > maxNum:
                    maxNum = leftString + rightString
        return maxNum