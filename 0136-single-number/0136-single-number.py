class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsMap = Counter(nums)
        return list(numsMap.keys())[list(numsMap.values()).index(1)]