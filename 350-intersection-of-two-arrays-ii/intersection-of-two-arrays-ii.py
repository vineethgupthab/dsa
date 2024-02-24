class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final_result = []
        nums1_vals = defaultdict(lambda: 0)
        for val in nums1:
            nums1_vals[val]+=1
        nums2_vals = dict()
        for val in nums2:
            if val in nums2_vals:
                nums2_vals[val]+=1
            else:
                nums2_vals[val]=1
        for key in nums2_vals:
            if nums1_vals[key]>0:
                temp = [key for i in range(min(nums1_vals[key], nums2_vals[key]))]
                final_result.extend(temp)
        return final_result
        
        
