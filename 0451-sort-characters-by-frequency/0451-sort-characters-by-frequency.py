class Solution(object):
    def frequencySort(self, s):
        

        freq = {} 

        for ch in s :

            freq[ch] = freq.get(ch, 0)+1

        ans = ""
        
        for ch  , count in sorted(freq.items() , key = lambda x :x[1] , reverse =True):

            ans += ch * count 

        return ans 



        