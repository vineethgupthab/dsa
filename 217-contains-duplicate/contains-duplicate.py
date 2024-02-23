class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_seen = dict()
        for num in nums:
            if num in nums_seen:
                return True
            else:
                nums_seen[num]=1
        return False