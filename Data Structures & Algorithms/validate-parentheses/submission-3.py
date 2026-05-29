class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        my_dict = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in ['(', '[', '{']:
                my_stack.append(char)
            elif char in [')', ']', '}']:
                if len(my_stack) != 0:
                    removed = my_stack.pop()
                    if removed == my_dict[char]:
                        continue;
                    else: return False
                else: return False
        return len(my_stack) == 0

         # cases: "{}()[]", "[({})]"   
        