class Solution(object):
    def maxArea(self, height):
        

        l = 0 
        r = len(height) -1

        max_area=0

        while l < r : 

            wd  = r - l
            he = min(height[l] , height[r])

            curr_area = wd * he

            max_area = max(max_area, curr_area)

            if height[l] < height[r]:

                l +=1
            else :
                r-= 1

        return max_area
        