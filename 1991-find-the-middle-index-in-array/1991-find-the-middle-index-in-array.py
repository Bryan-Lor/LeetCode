class Solution(object):
    def findMiddleIndex(self, nums):
        # This is similar to finding the pivot index where left side == right side
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == totalSum - leftSum - nums[i]:
                return i
            else:
                leftSum += nums[i]
        return -1