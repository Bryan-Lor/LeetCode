class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        sum, i = 0, 0
        while i <= len(s):
            try:
                if roman[s[i]] < roman[s[i+1]]:
                    sum += roman[s[i+1]] - roman[s[i]]
                    i+=2
                else:
                    sum += roman[s[i]]
                    i += 1
            except:
                try: sum += roman[s[i]]
                except: pass
                break
        return sum