class Solution(object):
    def containsDuplicate(self, nums):
        

        freq = {} 

        for num  in nums:

            freq[num] = freq.get(num ,0) +1

        
        for i in range(len(nums)):

            if freq[nums[i]] != 1 :
                return True

        return False 
        