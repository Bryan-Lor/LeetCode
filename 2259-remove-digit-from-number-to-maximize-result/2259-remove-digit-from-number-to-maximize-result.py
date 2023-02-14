class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # O(N^2) Brute Force Solution that creates a new string at each target digit and stores the highest number
        
        maxNum = ""
        for i in range(len(number)):
            if number[i] == digit:
                newString = number[:i] + number[i+1:]
                if newString > maxNum:
                    maxNum = newString
        return maxNum