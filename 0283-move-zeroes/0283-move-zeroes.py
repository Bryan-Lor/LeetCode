class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # O(n) solution. Iteratively scan and delete every zero.
        # For every zero deleted, additionally add it back into the
        # end of the list.
        zeroIndexes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroIndexes.append(i)
        
        counter = 0
        for i, zeroIndex in enumerate(zeroIndexes):
            del nums[zeroIndex-counter]
            zeroIndexes[i] = 0
            counter+=1
        nums.extend(zeroIndexes)
                