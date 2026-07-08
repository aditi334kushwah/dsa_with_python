class Solution(object):
    def subarraysDivByK(self, nums, k):
       

        prefix= {0 : 1}
        curr_sum = 0
        count = 0

        for num in nums :

            curr_sum += num
            remainder = curr_sum % k

            if remainder in prefix :

                count += prefix[remainder]

            if remainder  in prefix :

                prefix[remainder] += 1

            else :

                prefix[remainder] = 1
        

        return count 