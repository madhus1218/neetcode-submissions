class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for i in range(len(arr)):
        #     if i == len(arr) - 1:
        #         arr[i] = -1
        #         break
        #     temp = arr[i + 1: len(arr)]
        #     arr[i] = max(temp)
        # return arr
        
        max_seen = -1
        for i in range(len(arr) -1, -1, -1):
            curr = arr[i]
            arr[i] = max_seen

            if curr > max_seen:
                max_seen = curr
        return arr
            