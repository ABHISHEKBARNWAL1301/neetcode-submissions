class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def fun(i, j) -> int:
            if i < 0 or j < 0:
                return 0
            
            if (i, j) in mp:
                return mp[(i, j)]

            if text1[i] == text2[j]:
                mp[(i, j)] = 1 + fun(i-1, j-1)
            else:
                mp[(i, j)] = max(fun(i-1, j), fun(i, j-1))
            
            return mp[(i, j)]

            

        mp = defaultdict(tuple)
        i, j = len(text1)-1, len(text2)-1
        return fun(i, j)
        

