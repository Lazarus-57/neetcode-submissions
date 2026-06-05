class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        maxlength=0
        for num in set1:
            if num-1 not in set1:
                current=num
                length=1
                while current+1 in set1:
                    current+=1
                    length+=1
                maxlength=max(maxlength,length)
        return maxlength