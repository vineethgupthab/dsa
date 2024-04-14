class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        final_list = [[],[]]
        for num in nums1:
            if num in nums2:
                pass
            else:
                final_list[0].append(num)
        for num in nums2:
            if num in nums1:
                pass
            else:
                final_list[1].append(num)
        return final_list