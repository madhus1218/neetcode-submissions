class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        occurances = {}
        nums.sort()
        for num in nums:
            occurances[num] = occurances.get(num, 0) + 1
        for num in reversed(nums):
            if occurances[num] > 1:
                continue
            return num
        return -1


        