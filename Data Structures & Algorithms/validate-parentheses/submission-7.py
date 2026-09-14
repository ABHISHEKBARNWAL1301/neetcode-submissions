class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in ('{','[','('):
                st.append(i)
            else:
                if  st and ((st[-1] == '{' and i == '}') or (st[-1] == '[' and i == ']') or (st[-1] == '(' and i == ')')):
                    elem = st.pop()
                else:
                    return False

        return True if not st else False
                
