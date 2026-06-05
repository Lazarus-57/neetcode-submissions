class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1=0 
        p2=len(nums)-1
        middle=(p1+p2)//2
        while p1<=p2:
            if nums[middle]<target:
                p1=middle+1
                middle=(p1+p2)//2
            elif nums[middle]>target:
                p2=middle-1
                middle=(p1+p2)//2
            elif nums[middle]==target:
                return middle
                break
        return -1