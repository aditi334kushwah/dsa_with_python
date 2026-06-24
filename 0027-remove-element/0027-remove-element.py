class Solution(object):
    def removeElement(self, nums, val):
        
        k = 0
        for i in range(len(nums)):

            if val != nums[i] :
                
                nums[k] = nums[i]
                k+=1
            

        return k
        