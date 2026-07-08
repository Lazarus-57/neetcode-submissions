class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remaining_sum, path, start_index):
            #Base Cases
            #Reached the target
            if remaining_sum ==0:
                result.append(list(path))
                return
            
            #Overshot the target
            if remaining_sum<0:
                return

            #Ran out of numbers:
            if start_index >=len(nums):
                return

            #Decisions
            #Choice 1 - Include current number
            path.append(nums[start_index])

            backtrack(remaining_sum - nums[start_index], path, start_index)

            #Backtrack
            path.pop()

            #Choice 2 - Skip current number
            backtrack(remaining_sum, path, start_index+1)
        
        backtrack(target,[],0)
        return result
