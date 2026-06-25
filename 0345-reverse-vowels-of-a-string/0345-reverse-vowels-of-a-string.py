class Solution(object):
    def reverseVowels(self, s):
        
        start = 0
        end = len(s)-1

        s = list(s)

        temp = ['a', 'e' ,'i' , 'o'  ,'u','A','E','I','O','U']

        while start < end :

            while start < end and s[start] not in temp :
                start += 1
            
            while start < end and s[end] not in temp :
                end -= 1

            s[start], s[end] = s[end], s[start]

            start += 1
            end -= 1

        return "".join(s)

        