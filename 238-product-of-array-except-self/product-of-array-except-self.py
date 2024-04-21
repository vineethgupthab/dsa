class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltor_products = [1]*len(nums)
        for i in range(1,len(nums)):
            ltor_products[i] = nums[i-1]*ltor_products[i-1]
        
        rtol_products = [1]*len(nums)
        for i in range(len(nums)-2, -1,-1):
            rtol_products[i] = nums[i+1]*rtol_products[i+1]
        
        return [ltor_products[i]*rtol_products[i] for i in range(len(ltor_products))]

