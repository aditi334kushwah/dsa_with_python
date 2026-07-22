class Solution(object):
    def dailyTemperatures(self, temperatures):
           
        n = len(temperatures)

        res=[0]*n
        st  = []
     
        st.append(n-1)

        res[n-1] = 0

        for i in range(n-2,-1,-1) :

            while st and temperatures[st[-1]] <= temperatures[i] :

                st.pop()
                
            
            if st :

                res[i] = st[-1] - i


            st.append(i)

        return res


        