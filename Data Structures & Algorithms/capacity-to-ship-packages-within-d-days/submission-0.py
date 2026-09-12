class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def is_feasible(mid):
            day = 0
            summ = 0
            for weight in weights:
                if summ + weight <= mid:
                    summ += weight
                else:
                    day += 1
                    summ = weight
            
            return day < days
        
        
        maxm = sum(weights)
        minm = max(weights)

        while minm < maxm:
            mid = (minm + maxm)//2

            if is_feasible(mid):
                maxm = mid
            else:
                minm = mid + 1
            
        return maxm


        