class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0; j = len(height)-1
        while i<j:
            y = min(height[i],height[j])
            x = j-i
            max_area = max(max_area, x*y)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area
            