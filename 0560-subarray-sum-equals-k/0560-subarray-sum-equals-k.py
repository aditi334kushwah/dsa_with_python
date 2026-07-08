class Solution(object):
    def subarraySum(self, nums, k):

        prefix_sum = { 0 : 1}
        summ = 0
        count = 0

        for num in nums:

            summ += num 
            
            if summ - k in prefix_sum :

                count += prefix_sum[summ-k]

            if summ in prefix_sum :

                prefix_sum[summ] += 1

            else :

                prefix_sum[summ] = 1

        return count 




        
        