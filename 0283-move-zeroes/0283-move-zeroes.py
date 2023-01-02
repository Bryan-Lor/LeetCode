class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # O(n) solution. 
        zeroIndexes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroIndexes.append(i)
        print(zeroIndexes)
        
        counter = 0
        for i, zeroIndex in enumerate(zeroIndexes):
            del nums[zeroIndex-counter]
            zeroIndexes[i] = 0
            counter+=1
        nums.extend(zeroIndexes)