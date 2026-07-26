class Solution(object):
    def backspaceCompare(self, s, t):
        

        def build(st):
            stack = []

            for ch in st :

                if ch == '#':

                    if stack :
                        stack.pop()

                else :

                    stack.append(ch)

            return "".join(stack)

        return build(s) == build(t)
        