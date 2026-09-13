class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def feasible(number):
            hour=0
            print(number)
            for pile in piles:
                hour += math.ceil(pile/number)   
            if hour <= h:
                return True
            else:
                return False

        l, r = 1, max(piles)

        while l < r:
            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l = mid+1
        
        return r


        