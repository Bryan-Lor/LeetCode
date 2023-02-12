class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(log n) Solution using binary search to figure out where to place the target number.
        l = 0
        r = len(nums) - 1
        
        while (l <= r):
            m = (l + r) // 2            
            if  nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            if nums[m] < target:
                l = m + 1
        if(target > nums[m]):
            return m + 1
        else:
            return m