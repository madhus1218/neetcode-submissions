class Solution:
    def scoreOfString(self, s: str) -> int:
        my_dict = {}
        score = 0
        for i in range(len(s) - 1, -1, -1):
            my_dict[s[i]] = ord(s[i])
            if i == len(s) - 1:
                continue
            score += abs(my_dict[s[i + 1]] - my_dict[s[i]])
        return score