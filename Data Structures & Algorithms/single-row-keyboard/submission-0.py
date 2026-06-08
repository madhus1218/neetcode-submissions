class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        letters = {}
        temp = 0
        summ = 0

        for i, char in enumerate(keyboard):
            letters[char] = i

        for char in word:
            summ += abs(letters[char] - temp)
            temp = letters[char]
        
        return summ
