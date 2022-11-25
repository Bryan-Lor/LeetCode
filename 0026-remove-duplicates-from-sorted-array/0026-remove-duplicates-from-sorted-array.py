class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Sliding Window Technique. Using two pointers, constantly move right pointer
        # and if previous is not the same, update left pointer to current right pointer.
        # Additionally add l each time to l in order to count unique numbers.
        
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l