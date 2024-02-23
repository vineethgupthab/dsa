class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_freq = dict()
        for i in nums:
            if i in nums_freq:
                nums_freq[i]+=1
            else:
                nums_freq[i] = 1
        if sorted(nums_freq.values(), reverse=True)[0]>=2:
            return True
        else:
            return False