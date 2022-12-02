class Solution(object):
    def pivotIndex(self, nums):
        # Solution where you iterate through list counting up the left sum and comparing it to the right sum. 
        
#         # Brute Force Iteration O(n^3)
#         for i in range(0, len(nums)):
#             left = sum(nums[:i])
#             right = sum(nums[i+1:])
                
#             if(left == right):
#                 return i
#         return -1

#         # O(n^2) more optimized solution
#         leftSum = 0
#         for i in range(len(nums)):
#             leftSum += nums[i]
#             if leftSum == sum(nums[i:]):
#                 return i
#         return -1

        # O(n) optimized solution
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == totalSum - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        return -1