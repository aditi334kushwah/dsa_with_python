class Solution(object):
    def reverseString(self, s):

        st = 0
        ed = len(s)-1

        while st< ed :

            s[st],s[ed] = s[ed],s[st]

            st += 1
            ed -= 1