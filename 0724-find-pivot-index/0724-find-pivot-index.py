class Solution(object):
    def pivotIndex(self, nums):
#         Brute Force Iteration O(n^3)
#         for i in range(0, len(nums)):
#             left = sum(nums[:i])
#             right = sum(nums[i+1:])
                
#             if(left == right):
#                 return i
#         return -1

#         # Unsorted Binary Search Algorithm Implimentation O(log n)
#         def binarySearch(nums, left = 0, right = len(nums)-1):
#             mid = len(nums)-1 // 2
#             print(left, right)
#             while left <= right:
#                 leftSum = sum(nums[:mid])
#                 rightSum = sum(nums[mid+1:])
                
#                 print(mid, leftSum, rightSum)
                
#                 if leftSum == rightSum:
#                     return mid
#                 elif leftSum < rightSum:
#                     mid = len(nums[:mid])+ 1
#                 else:
#                     mid -= 1
#             return -1
        
#         return binarySearch(nums)

        # O(n^2) more optimized solution
        leftSum = 0
        for i in range(len(nums)):
            leftSum += nums[i]
            #print(i, leftSum, sum(nums[i:]))
            if leftSum == sum(nums[i:]):
                return i
        return -1