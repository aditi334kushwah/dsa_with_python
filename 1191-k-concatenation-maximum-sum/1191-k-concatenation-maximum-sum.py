class Solution(object):
    def kConcatenationMaxSum(self, arr, k): 

        def kadne(arr) :

            curr = arr[0]
            bestending = arr[0]

            for i in range(1 , len(arr)):

                curr = max(curr + arr[i]  , arr[i])
                bestending = max(bestending , curr)

            return bestending
        
        
        total_sum = sum(arr) 

        if k == 1 :

            return max(0 ,  kadne(arr))

        two_arr = arr + arr

        max_two = kadne(two_arr)

        if total_sum <= 0 :

            return max(0, max_two ) % (10**9 + 7)

        else :

            t = (k-2)*total_sum

            return  (max_two + t) % (10**9 + 7)

