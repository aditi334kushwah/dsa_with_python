class Solution(object):
    def runningSum(self, nums):
        
        n  = len(nums)
        running = [0] *n
        
        running[0] = nums[0]

        for  i in range(1, n):

            running[i] = running[i-1] + nums[i]


        return running 

