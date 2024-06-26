class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        j = k
        max_sum = sum(nums[:k])
        greatest_sum = max_sum
        i = 0
        while j<len(nums) and i<j:
            max_sum+=nums[j]
            max_sum-=nums[i]
            greatest_sum = max(max_sum, greatest_sum)
            i+=1
            j+=1
        return greatest_sum/k