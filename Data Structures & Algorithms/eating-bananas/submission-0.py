import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)

        def finished(k):
                    hours=0
                    for i in piles:
                        hours+=math.ceil(i/k)
                    return hours<=h

        while left<=right:
            mid=(left+right)//2
            if finished(mid)==True:
                right=mid-1
            else:
                left=mid+1 
        return left
    
