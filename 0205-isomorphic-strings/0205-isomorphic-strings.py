class Solution(object):
    def isIsomorphic(self, s, t):
        
        if len(s) != len(t) :

            return False 

        mapS = {} 
        mapT = {} 

        for ch1, ch2 in zip(s,t):

            if ch1 in mapS:

                if mapS[ch1] != ch2:

                    return False 
            else :
                mapS[ch1] = ch2

            
            if ch2 in mapT :

                if mapT[ch2] != ch1:

                    return False 
            else :

                mapT[ch2] = ch1

        return True
        