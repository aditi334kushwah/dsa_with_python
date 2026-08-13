class Solution(object):
    def mySqrt(self, x):
       
        low = 0 
        high = x 

        ans = 0 
        while low <= high :

            mid = (low +high) // 2
            sqr = mid * mid 

            if sqr == x :

                return mid 

            elif sqr <= x :

                ans = mid 
                low = mid + 1

            else :

                high = mid -1

        return ans 
