class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" 
        n = len(s)

        for i in range(0, n):
            # odd length
            l, r = i, i
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]

            # even length
            l, r = i, i + 1
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]
        
        return res