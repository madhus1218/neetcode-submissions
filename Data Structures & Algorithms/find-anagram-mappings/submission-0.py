class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []
        my_list = {}
        for i, num in enumerate(nums2):
            my_list[num] = i
        for num in nums1:
            mapping.append(my_list[num])
        return mapping
            
