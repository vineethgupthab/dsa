class Solution:
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
        return count