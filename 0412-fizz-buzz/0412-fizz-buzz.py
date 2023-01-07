class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # O(n) solution that iteratively checks if sequential numbers leading to
        # n is divisable by 3 and 5. Then append corresponding fizz/buzz/fizzbuzz/i 
        # value into a list and return it after the loop.
        l = []
        for i in range(1, n+1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
                
            if s == "":
                l.append(str(i))
            else:
                l.append(s)
        return l