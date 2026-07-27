class Solution(object):
    def evalRPN(self, tokens):
        
        stack = [] 

        for ch in tokens :

            if ch == '+' :

                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)


            elif ch == '-':

                a = stack.pop()
                b = stack.pop()
                stack.append(b -a)

            elif ch == '*' :

                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

            
            elif ch == '/' :

                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b ) / a))

            
            else :

                stack.append(int(ch))

        return stack[-1]