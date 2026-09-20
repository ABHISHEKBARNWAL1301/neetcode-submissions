class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
 
        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []

        def dfs(idx, s):
            if idx == len(digits):
                ans.append(s)
                return

            for ch in mp[digits[idx]]:
                dfs(idx+1, s+ch)
        
        if len(digits) == 0:
            return []
        dfs(0, "")
        return ans
