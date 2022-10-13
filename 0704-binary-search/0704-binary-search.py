class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # #Fast Solution
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        
        
        # Binary Search Algorithm
        def binarySearch(nums, target, leftPointer = 0, rightPointer = len(nums)-1):
            while leftPointer <= rightPointer:
                midPointer = (leftPointer + rightPointer) // 2
                if nums[midPointer] == target:
                    return midPointer
                elif nums[midPointer] < target:
                    leftPointer = midPointer + 1
                else:
                    rightPointer = midPointer - 1
            return -1
        
        return binarySearch(nums, target)