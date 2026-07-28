class Solution(object):
    def wordPattern(self, pattern, s):
       
        words = s.split()

        if len(pattern) != len(words) :
            return False 

        mapP = {} 
        mapS = {} 

        for ch1, ch2 in zip(pattern , words):

            if ch1  in mapP:
                if mapP[ch1] != ch2:
                    return False 
            
            else :

                mapP[ch1]   = ch2
        
            if ch2 in mapS :

                if mapS[ch2] != ch1:
                    return False 
            else :
                mapS[ch2] = ch1

        
        return True