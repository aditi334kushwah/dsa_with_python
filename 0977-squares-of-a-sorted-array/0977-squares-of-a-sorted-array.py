class Solution(object):
    def sortedSquares(self, nums):
        

        pos = []
        neg = []
        

        for num in nums :

            if num <0 :

                neg.append(num)
            else :
                pos.append(num)

        left = 0 
        right = len(neg) - 1
        while left < right :

            neg[left] , neg[right] = neg[right] , neg[left]

            left += 1 
            right -= 1

        pos = [x *x for x in pos]
        neg = [ x*x for x in  neg]

        n = len(pos) 
        m = len(neg) 

        ans = [0]* (m+n)
        
        t = n-1
        v = m -1
        k= m +n -1

        while t >= 0 and v >= 0 :

            if pos[t] > neg[v] :
                ans[k] = pos[t] 

                t-= 1
            else :

                ans[k] = neg[v]

              
                v -= 1

            k -= 1
        
        while v >= 0 :
            
            ans[k] = neg[v]
            v -= 1
            k -= 1

        while t >= 0 :

            ans[k] = pos[t]
            k-= 1
            t -=1

        return ans