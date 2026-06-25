class Solution(object):
    def findMaxAverage(self, nums, k):

       
        low = 0 
        sum = 0
        ans = float('-inf')
        avg = 0

        for right in range(len(nums)):

            sum += nums[right]
            avg = sum/ float(k)

            if right - low + 1 ==k:

                ans = max(ans, avg)

                sum -= nums[low]
                low +=1

        return ans