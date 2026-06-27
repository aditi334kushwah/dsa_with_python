class Solution(object):
    def maxAbsoluteSum(self, nums):
        
        cs = nums[0]
        maxs = nums[0]

        cm = nums[0]
        mins = nums[0]

        for i in  range(1, len(nums)):

            cs = max(cs + nums[i] , nums[i])
            maxs = max(cs, maxs)

            cm = min(cm + nums[i] , nums[i])
            mins = min( mins , cm)

        return max(maxs , abs(mins))

        