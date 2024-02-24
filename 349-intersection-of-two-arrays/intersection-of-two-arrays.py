class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        freq = defaultdict(lambda:0)
        for num in nums1:
            freq[num]=1
        for num in nums2:
            if freq[num]==1:
                result.add(num)
        return result