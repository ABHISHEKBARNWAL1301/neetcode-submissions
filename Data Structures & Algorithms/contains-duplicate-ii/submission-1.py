class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = defaultdict(list)
        for idx, num in enumerate(nums):
            if mp[num] and abs(mp[num][-1] - idx) <= k:
                return True
            mp[num].append(idx)

        return False