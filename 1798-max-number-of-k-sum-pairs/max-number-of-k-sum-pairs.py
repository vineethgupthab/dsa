'''class Solution:
    def maxOperations(self,nums, k):
        left = 0; right = len(nums)-1; count = 0
        nums.sort()
        while left<right:
            if nums[left]+nums[right]==k:
                count+=1
                nums.pop(left)
                left=left
                right=right-1
                nums.pop(right)
                right=right-1
                continue
            elif nums[left]+nums[right]<k:
                left+=1
            else:
                right-=1
        return count'''

class Solution:
    def maxOperations(self, nums, k):
        count = 0
        num_freq = {}
        
        for num in nums:
            complement = k - num
            if complement in num_freq and num_freq[complement] > 0:
                count += 1
                num_freq[complement] -= 1
            else:
                num_freq[num] = num_freq.get(num, 0) + 1
        
        return count
