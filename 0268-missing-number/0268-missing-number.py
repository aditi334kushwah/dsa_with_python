class Solution(object):
    def missingNumber(self, nums):
        
        nums.sort()
        low = 0 
        high = len(nums)-1

        while low <= high :

            mid = (low + high) //2

            if nums[mid] == mid :

                low = mid + 1

            else :

                high = high - 1


        return low
