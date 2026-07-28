class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        f = {}  

        for  ch in magazine :

            f[ch] = f.get(ch , 0) +1

        
        for c in ransomNote :

            if c not in f :

                return False 

            f[c] -= 1

            if f[c] < 0 :

                return False 

        return True
        