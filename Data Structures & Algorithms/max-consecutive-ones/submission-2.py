class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxx = 0
        for i, num in enumerate(nums):
            if num == 1:
                counter += 1
            else:
                counter = 0
            if counter > maxx:
                maxx = counter
        return maxx
        