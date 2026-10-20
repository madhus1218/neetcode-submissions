class Solution:
    def climbStairs(self, n: int) -> int:
        T = [0]*(n+1)
        if n < 3:
            return n
        T[1] = 1
        T[2] = 2
        for i in range(len(T)):
            if i >=3:
                T[i] = T[i-1] + T[i-2]
        return T[n]

        