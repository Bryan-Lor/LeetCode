class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n) solution that constructs a dictionary with the amount of times
        # the element shows. Then you simply retrieve the element that shows
        # only once in constant time O(1).
        numsMap = Counter(nums)
        return list(numsMap.keys())[list(numsMap.values()).index(1)]