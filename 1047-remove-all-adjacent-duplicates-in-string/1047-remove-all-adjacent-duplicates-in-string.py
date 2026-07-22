class Solution(object):
    def removeDuplicates(self, s):
        
        stack = []

        for ch in s  :

            if len(stack) ==0:

                stack.append(ch)
                continue
            
            if len(stack)!= 0 and  stack[-1] == ch: 

                stack.pop()
                continue
            
            stack.append(ch)
            

        return "".join(stack)
                

        