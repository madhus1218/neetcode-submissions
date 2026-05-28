class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # need to check if each characted exists and the correct number of times
        if len(t) != len(s):
            return False
        my_map_s = {}
        my_map_t = {}
        for char in s:
            if char in my_map_s:
                my_map_s[char] += 1
            else:
                my_map_s[char] = 1
        for char in t:
            if char not in my_map_s:
                return False
            # if the key exists, check if the number of times it exists in s and t are the same
            if char in my_map_t:
                my_map_t[char] += 1
            else:
                my_map_t[char] = 1
        return my_map_s == my_map_t


        