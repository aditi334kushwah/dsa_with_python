class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        
        prefix = [0]*len(arr) 
        prefix[0] = arr[0]
        for i in range(1, len(arr)) :

            prefix[i] = prefix[i-1] + arr[i]


        res = 0
        for start in range(len(arr)):

            for end in range(start , len(arr)):

                if (end - start + 1) % 2 ==1 :

                    if start == 0 :
                        res+= prefix[end]

                    else:
                        res += prefix[end] - prefix[start-1]

        return res
        