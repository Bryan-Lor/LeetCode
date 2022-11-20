class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        sum = 0
        
        i = 0     
        while i <= range(len(s)):
            # Tries to check if next number is greater
            try:
                # If next number is greater, then subtract its value from current
                if roman[s[i]] < roman[s[i+1]]:
                    #print("added", roman[s[i+1]] - roman[s[i]], "subtracted")
                    sum += roman[s[i+1]] - roman[s[i]]
                    i+=2
                # Otherwise just add itself
                else:
                    #print("added", roman[s[i]])
                    sum += roman[s[i]]
                    i += 1
            except:
                # No next number, so it is the last element
                try:
                    sum += roman[s[i]]
                except:
                    pass
                #print("No next number")
                break
        #print("Total", sum)
        return sum