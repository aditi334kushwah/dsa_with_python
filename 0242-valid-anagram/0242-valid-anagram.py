class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t) :
            return False 

        f = {}

        for n in s:

            f[n] = f.get( n,0) +1

        for ch in t :

            if not ch in f :
                return False 
            

            f[ch] -= 1

            if f[ch] < 0:
                return False 

        return True 

        

        

        