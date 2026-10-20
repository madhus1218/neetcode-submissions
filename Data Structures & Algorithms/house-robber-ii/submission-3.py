class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        T1 = [0] * len(nums)
        T1[0] = 0
        T1[1] = nums[0]
        for i in range(2, len(nums)):   
            T1[i] = max(T1[i - 1], T1[i-2] + nums[i-1])

        T2 = [0] * len(nums)
        T2[0] = 0
        T2[1] = nums[1]
        for i in range(2, len(nums)):   
            T2[i] = max(T2[i - 1], T2[i-2] + nums[i])

        return max(T1[len(nums)-1], T2[len(nums)-1])
        