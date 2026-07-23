class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            
            if self.calcTime(piles, mid) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            
    def calcTime(self, piles: List[int], rate: int) -> int:
        t = 0
        for pile in piles:
            if pile % rate == 0:
                t += pile // rate
            else:
                t += pile // rate + 1
        return t
