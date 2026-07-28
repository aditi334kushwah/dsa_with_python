class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        f = {}

        for n in nums : 

            f[n] = f.get(n , 0) +1


        sf = sorted(f.items(), key = lambda  x : x[1] , reverse = True)


        return sf[0][0]

        