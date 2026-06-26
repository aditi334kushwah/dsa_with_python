from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        
        if len(s1) > len(s2) :
            return False

        f_count = Counter(s1)
        window = Counter()
        low =0

        for high in range(len(s2)):

            window[s2[high]] +=1

            if high - low +1 > len(s1):

                window[s2[low]] -= 1

                if window[s2[low]] == 0:
                    del window[s2[low]]

                low +=1


            if high -low+1 == len(s1) :
                if window == f_count :
                    return True
        
        return False 