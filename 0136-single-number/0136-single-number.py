class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n) solution that constructs a dictionary with the amount of times
        # the element shows, then you simply retrieve the element that shows
        # only once [O(1) operation].
        numsMap = Counter(nums)
        return list(numsMap.keys())[list(numsMap.values()).index(1)]