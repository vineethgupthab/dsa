class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        count = 0
        max_nums = 0
        while j < len(nums):
            if nums[j] == 0:
                count += 1
            
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i += 1
                
            max_nums = max(max_nums, j - i + 1)
            j += 1
        
        return max_nums
