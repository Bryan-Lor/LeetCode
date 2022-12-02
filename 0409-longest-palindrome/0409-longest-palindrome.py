class Solution:
    def longestPalindrome(self, s: str) -> int:
        # O(n) Solution where you create a set from the string and iterate through that set counting the characters and appending the even values into a list which the sum will be returned
        countList = []
        setValues = set(s)        
        for char in setValues:
            count = s.count(char)
            if count > 1 and count % 2 == 0:
                countList.append(count)
            else:
                countList.append(count - 1)
                
        sumAmount = sum(countList)
        if sumAmount == len(s):
            return sumAmount
        else:
            return sumAmount + 1