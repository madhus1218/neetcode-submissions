class Solution:
    def rob(self, nums: List[int]) -> int:
        T = [0]*(len(nums) + 1)
        T[0] = 0
        T[1] = nums[0]
        for i in range(2, len(nums) + 1):
            T[i] = max(T[i-1], T[i-2] + nums[i-1])
        return T[len(nums)]
        