class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        longer = max(word1,word2, key=len)
        shorter = min(word1,word2, key=len)
        result = ""
        for i, char in enumerate(shorter):
            left = word1[i]
            right = word2[i]
            result += left
            result += right
        leftover = longer[len(shorter):]
        return result + leftover