class Solution(object):
    def intersection(self, nums1, nums2):

        seen = set()

        for num in nums1 :
            seen.add(num)

        res = []
        for  n in nums2 :
            
            if n in seen :

                if n not in res :
                    res.append(n)

            
        return res

       
        