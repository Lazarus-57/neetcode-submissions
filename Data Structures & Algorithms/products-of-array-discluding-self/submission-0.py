class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finallist=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i!=j:
                    product*=nums[j]
            finallist.append(product)
        return finallist