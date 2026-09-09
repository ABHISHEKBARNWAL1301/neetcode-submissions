class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def helper(s):
            count = [0]*26
            for ss in s:
                count[ord(ss)-ord('a')] += 1
            return count

        groups = defaultdict(list)
        for s in strs:
            key = helper(s)
            groups[tuple(key)].append(s)
        
        return list(groups.values())
