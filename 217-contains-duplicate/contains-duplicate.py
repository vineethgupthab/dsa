class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''nums_freq = dict(); max = 0
        for i in nums:
            if i in nums_freq:
                nums_freq[i]+=1
                max = nums_freq[i]
            else:
                nums_freq[i] = 1
        if max>=2:
            return True
        else:
            return False'''
        nums.sort()
        i=0
        j=i+1
        while j<len(nums):
            if nums[i]==nums[j]:
                return True
            i+=1
            j+=1
        return False