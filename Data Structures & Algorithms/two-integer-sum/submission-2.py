class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []
        my_dict ={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                result.extend([my_dict[complement], i])
                return result
            my_dict[nums[i]] = i 
        return result


        