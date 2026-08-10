class Solution(object):
    def minEatingSpeed(self, piles, h):
       
        def findHour(piles, speed):

            hours =0 

            for pile  in piles:

                hours  += pile // speed

                if pile % speed != 0 :
                    hours += 1
            
            return hours

        low = 1
        high = max(piles)
        res = -1

        while low <= high :

            mid = (low + high) //2

            hours = findHour(piles,  mid) 

            if hours > h :

                low = mid +1

            else :

                res = mid 
                high = mid -1 

        return res
                    
        
        