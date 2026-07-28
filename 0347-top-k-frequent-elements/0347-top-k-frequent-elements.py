class Solution(object):
    def topKFrequent(self, nums, k):
        
        f = {}

        for num in nums :

            f[num] = f.get(num , 0) +1

        

        sorted_f  = sorted(f.items(), key = lambda x : x[1] , reverse = True)


        ans = [] 
        for i in range(k) :

            ans.append(sorted_f[i][0])
        
        return ans 