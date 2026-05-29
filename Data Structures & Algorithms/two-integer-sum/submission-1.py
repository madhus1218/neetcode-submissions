class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []
        # j = 0
        # for i in range(len(nums)):
        #     if i != j:
        #         if nums[i] + nums[j] == target:
        #             result.extend([j, i])
        #         j+=1
        # return result

        result = []
        my_dict ={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                result.extend([my_dict[complement], i])
            my_dict[nums[i]] = i       # key-num : value-index
        return result


        