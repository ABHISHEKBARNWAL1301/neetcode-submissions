class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def fun(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = fun(i+1, j+1)
            else:
                memo[(i, j)] = 1 + min(fun(i, j+1), fun(i+1, j), fun(i+1, j+1))
            
            return memo[(i, j)]
        
        memo = {}
        m, n = len(word1), len(word2)  
        return fun(0, 0)