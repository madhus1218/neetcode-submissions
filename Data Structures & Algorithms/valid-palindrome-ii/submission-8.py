class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left] == s[right]:
                left +=1
                right -= 1
            else:
                subLeft = s[left + 1:right + 1]
                subRight = s[left: right]
                if subLeft == subLeft[::-1]:
                    return True
                elif subRight == subRight[::-1]:
                    return True
                else: return False
        return True

                

        


            