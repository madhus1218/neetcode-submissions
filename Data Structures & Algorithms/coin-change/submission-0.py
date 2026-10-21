class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        T = [float('inf')] * (amount + 1)
        T[0] = 0

        for i in range (1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    T[i] = min(T[i-c] + 1, T[i])
        
        if T[len(T) - 1] == float('inf'):
            return -1
        else:
            return T[len(T) - 1]

        