class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        booleans = []
        for i in candies:
            if (i+extraCandies) < max_val:
                booleans.append(False)
            else:
                booleans.append(True)
        return booleans
        