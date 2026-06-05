class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    list_result.append(i)
                    list_result.append(j)
                    return list_result