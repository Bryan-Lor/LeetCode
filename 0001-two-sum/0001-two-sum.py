class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) solution where you iteratively go through each item and search if
        # target - nums[i] exists within the list. If so, simply return the two indexes
        for i in range(len(nums)):
            complimentaryNumber = target - nums[i]
            if complimentaryNumber in nums and nums.index(complimentaryNumber) != i:
                return [i, nums.index(complimentaryNumber)]
        return []