class Solution(object):
    def countGoodSubstrings(self, s):
       
        low =count = 0

        for high in range(len(s)):

            if high -low +1 > 3:
                low+=1

            if high -low +1 == 3:

                if len(set(s[low:high+1])) ==3:
                    count +=1

        return count