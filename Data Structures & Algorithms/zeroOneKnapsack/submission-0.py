class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        T = [[0] * (capacity + 1) for _ in range(len(profit) + 1)]

        for i in range(1, len(profit) + 1):
            for j in range(1, capacity + 1):
                T[i][j] = T[i-1][j]

                if weight[i-1] <= j:
                    T[i][j] = max(T[i][j], T[i-1][j-weight[i-1]] + profit[i-1])

        return T[len(profit)][capacity]