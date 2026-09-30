class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" 
        n = len(s)

        def helper(l, r):
            nonlocal res
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]
        
        for i in range(0, n):
            helper(i, i)
            helper(i, i+1)

        return res