class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                nums.append("_")
            else: i += 1
            
        count = 0
        for num in nums:
            if num != "_":
                count+=1
        return count
                

                
        