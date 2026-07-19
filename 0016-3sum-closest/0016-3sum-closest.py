class Solution(object):
    def threeSumClosest(self, nums, target):
       

        nums.sort()
        n = len(nums)

        closest = nums[0]+ nums[1] +nums[2]

        for i in range(n-2):

            left = i +1
            right  = n-1

            while left < right :

                curr_closest= nums[i] +nums[left] +nums[right]

                if abs(curr_closest -target) < abs(closest - target) :

                    closest = curr_closest 


                if curr_closest < target :

                    left += 1

                else :
                     right -=1
                
        return closest 