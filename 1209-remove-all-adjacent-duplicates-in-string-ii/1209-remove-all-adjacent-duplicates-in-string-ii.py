class Solution(object):
    def removeDuplicates(self, s, k):
        
        st = [] 
        for ch in s:

            if st and st[-1][0] == ch :
                st[-1][1] +=1

                if st[-1][1]==k :
                    st.pop()

            else :

                st.append([ch , 1])     

        ans = [] 

        for char ,count in st :

            ans.append(char*count )

        
        return "".join(ans)