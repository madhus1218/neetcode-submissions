class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        T = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        return T[len(text1)][len(text2)]
        