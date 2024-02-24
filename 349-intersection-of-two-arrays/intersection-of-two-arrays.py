class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        present = set()
        for num in nums1:
            if num in nums2:
                present.add(num)
        return present
            