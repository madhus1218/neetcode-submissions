class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # too inefficient
        # for i, num in enumerate(nums):
        #     begin = nums[:i]
        #     after = nums[i+1:]
        #     if num in begin:
        #         return True
        #     elif num in after:
        #         return True
        # return False
        
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

                
        