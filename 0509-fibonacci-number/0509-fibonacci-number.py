class Solution(object):
#     # O(n) solution where you iteratively calculate the fibinacci number via two variables.
#     def fib(self, n):
#         if n < 2:
#             return n
        
#         n0 = 0
#         n1 = 1
#         for i in range(n-1):
#             fibNum = n0 + n1
#             n0 = n1
#             n1 = fibNum
#         return n1
    
    
    # O(n) solution where you recursively calculate the fibinacci number with memoization
    def fib(self, n, memo = {}):
        if n in memo:
            return memo[n]
        if n < 2:
            return n
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]