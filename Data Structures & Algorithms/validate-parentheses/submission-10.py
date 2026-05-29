class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        my_dict = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in my_dict.values():
                my_stack.append(char)
            elif char in my_dict:
                if my_stack:
                    removed = my_stack.pop()
                    if removed != my_dict[char]:
                        return False
                else: return False
        return len(my_stack) == 0
        