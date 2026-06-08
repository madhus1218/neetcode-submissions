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
        
"""
[5,7,3,9,4,9,8,3,1]
[1,3,3,4,5,7,8,9,9]
1:1, 3:2, 4:1, 5:1, 7:1, 8:1, 9:2
[9,9,8,7,5,4,3,3,1]

"""


        