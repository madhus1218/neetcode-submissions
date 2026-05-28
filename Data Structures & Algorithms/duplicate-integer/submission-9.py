class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # TOO INEFFICIENT
        # for i, num in enumerate(nums):
        #     begin = nums[:i]
        #     after = nums[i+1:]
        #     if num in begin:
        #         return True
        #     elif num in after:
        #         return True
        # return False
        
        # USING SORT()
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False


        # USING SET()
        # my_set = set()
        # for num in nums:
        #     if num in my_set:
        #         return True
        #     else:
        #         my_set.add(num)
        # return False

        return len(nums) > len(set(nums))



                
        