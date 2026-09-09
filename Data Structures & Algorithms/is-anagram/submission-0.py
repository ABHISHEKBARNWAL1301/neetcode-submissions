class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter = defaultdict(int)
        for ss in s:
            counter[ss] +=1
        
        for tt in t:
            counter[tt] -= 1
            if counter[tt] < 0:
                return False
        return True

        
        # return Counter(s) == Counter(t) 