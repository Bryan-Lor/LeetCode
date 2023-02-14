class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
#         removed = False
#         s = ""
#         for char in number:
#             if char == digit and not removed:
#                 removed = True
#                 continue
#             s += char
            
#         return s
        maxNum = ""
        for i in range(len(number)):
            if number[i] == digit:
                leftString = number[:i]
                rightString = number[i+1::]
                if leftString + rightString > maxNum:
                    maxNum = leftString + rightString
        return maxNum