class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        stack = []
        dic = {}

        for  num  in nums2 :

            while stack and stack[-1] < num :

                dic[stack.pop()] = num

            stack.append(num)

            
        while  stack :

            dic[stack.pop()]= -1

        
        res = []

        for num in nums1 :

            res.append(dic[num])

        return res

         