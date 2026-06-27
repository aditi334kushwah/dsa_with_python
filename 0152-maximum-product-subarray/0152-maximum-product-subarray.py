class Solution(object):
    def maxProduct(self, nums):
        
        curr_max = nums[0]
        curr_min =nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):

            v1= nums[i]
            v2 = curr_max*nums[i]
            v3 = curr_min*nums[i]

            curr_min= min(v1, min(v2,v3))
            curr_max = max(v1, max(v2,v3))

            max_product = max(max_product, max(curr_min, curr_max))

        return max_product
        