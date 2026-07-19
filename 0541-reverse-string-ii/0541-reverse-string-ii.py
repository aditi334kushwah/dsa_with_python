class Solution(object):
    def reverseStr(self, s, k):

        s = list(s)
        n = len(s)

        for i in range(0 , n, 2*k):

            left = i 
            right = min(i+k-1, n-1)

            while left < right :

                s[left] , s[right] = s[right], s[left]

                left += 1
                right -= 1

            
        return "".join(s)

       
        