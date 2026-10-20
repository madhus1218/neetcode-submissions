class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        T = [0]*(len(cost) + 1)
        for i in range(2, len(cost) + 1):
            T[i] = min(T[i-1] + cost[i-1], T[i-2]+cost[i-2])
        return T[len(cost)]
        