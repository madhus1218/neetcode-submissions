class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = {}
        total = 0
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        for num in counter:
            if num + 1 in counter:
                total += counter[num]
        return total