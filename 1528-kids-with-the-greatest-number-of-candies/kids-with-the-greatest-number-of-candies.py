class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        return [False if (i+extraCandies) < max_val else True for i in candies]
        