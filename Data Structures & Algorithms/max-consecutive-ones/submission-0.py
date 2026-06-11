class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxx = 0
        for i, num in enumerate(nums):
            if (i == len(nums)) and (num == 1):
                counter += 1
                return counter
            elif num == 1:
                counter += 1
            elif num == 0:
                counter = 0
            if counter > maxx:
                maxx = counter
        return maxx
        