class Solution:
    def isValid(self, s: str) -> bool:
        l1=[]
        close=0
        openn=0
        for i in s:
            if i in ('{','[','('):
                l1.append(i)
                openn+=1
            else:
                if openn > close:
                    elem = l1.pop()
                    if  (elem == '{' and i == '}') or (elem == '[' and i == ']') or (elem == '(' and i == ')'):
                        close += 1
                        continue
                    else:
                        return False
                else:
                    return False

                close+=1

        return close==openn
                
