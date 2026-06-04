class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip()
        num_of_spaces = [i for i, char in enumerate(stripped) if char == " "]
        if len(num_of_spaces) == 0:
            return len(stripped)
        sliced = num_of_spaces[len(num_of_spaces) - 1]
        return len(stripped[sliced + 1:])
        