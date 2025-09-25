class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "([{":
                st.append(i)
            else:
                if len(st)==0:
                    return False
                if (st[-1]=='(' and i==')') or (st[-1]=='[' and i==']') or (st[-1]=='{' and i=='}'):
                    st.pop()
                else:
                    return False
        return len(st)==0