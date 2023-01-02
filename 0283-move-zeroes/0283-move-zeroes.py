class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # O(n) solution. Iteratively scan and grab indexes of zeroes into a list.
        # For every zero found, delete it via index and add it back into the
        # end of the list.
        zeroIndexes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroIndexes.append(i)
        
        counter = 0
        for i, zeroIndex in enumerate(zeroIndexes):
            nums.pop(zeroIndex-counter)
            zeroIndexes[i] = 0
            counter+=1
        nums.extend(zeroIndexes)
                