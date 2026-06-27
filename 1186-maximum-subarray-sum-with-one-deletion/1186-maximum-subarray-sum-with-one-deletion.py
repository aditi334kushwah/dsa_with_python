class Solution(object):
    def maximumSum(self, arr):
        
        keep = arr[0]
        delete = 0 

        res = arr[0]
        for i in range(1 , len(arr)):

            new_keep = max( keep+arr[i] , arr[i])
            new_delete =max(delete+arr[i], keep)

            keep = new_keep
            delete = new_delete

            res= max( res , keep , delete)

        return res
        