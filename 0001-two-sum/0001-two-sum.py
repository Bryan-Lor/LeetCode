class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2) solution where you iteratively[O(n)] go through each item and search if
        # target - nums[i] exists within the list. If so, simply return the two indexes which .         # also takes [O(n)] times. O(n) * O(n) = O(n^2)
        # for i in range(len(nums)):
        #     complimentaryNumber = target - nums[i]
        #     if complimentaryNumber in nums and nums.index(complimentaryNumber) != i:
        #         return [i, nums.index(complimentaryNumber)]
        
    
        # O(n) solution that iteratively goes through each item and saves its 
        # complimentary number into a dictionary which will then be returned in O(1) time.
        # O(n) * O(1) = O(n)
        complimentMap = dict()        
        for i in range(len(nums)):
            complimentaryNumber = target - nums[i]
            if nums[i] in complimentMap:
                return [complimentMap[nums[i]], i]
            else:
                complimentMap[complimentaryNumber] = i