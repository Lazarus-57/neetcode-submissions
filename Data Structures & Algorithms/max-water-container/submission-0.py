class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        current_area=0
        while l<r:
            width=r-l
            height=min(heights[l],heights[r])
            new_area = width*height 
            if new_area>current_area:
                current_area=new_area

            if height==heights[l]:
                l+=1
            elif height==heights[r]:
                r-=1
        return current_area