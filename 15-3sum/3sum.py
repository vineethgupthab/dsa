class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(); results = []
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                summ = nums[left]+nums[i]+nums[right]
                if summ<0:
                    left+=1
                elif summ>0:
                    right-=1
                else:
                    target = [nums[i],nums[left],nums[right]]
                    results.append(target)
                    while left<right and nums[left] == target[1]:
                        left+=1
                    while left<right and nums[right] == target[2]:
                        right-=1
        return results