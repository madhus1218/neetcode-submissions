class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        for num in counter:
            if counter[num] >= len(nums)/2:
                return num
        return 0