class Solution(object):
    def maxSubarraySumCircular(self, nums):
        
        total_sum = sum(nums)
        cs= nums[0]
        max_sum = nums[0]

        cm= nums[0]
        min_sum = nums[0]

        res = nums[0]
        
        for i in range(1, len(nums)):

            cs = max(cs+nums[i ] , nums[i])
            max_sum = max(max_sum ,cs)

            cm = min(cm +nums[i] , nums[i])
            min_sum = min(min_sum , cm)

        if max_sum < 0:
            return max_sum

             
        return max(max_sum , total_sum-min_sum)