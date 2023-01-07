class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) solution that creates a set of the list and compares the length of both
        setNums = set(nums)
        return (True if len(setNums) != len(nums) else False)