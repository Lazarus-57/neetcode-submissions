class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_seen=set()
        for i in nums:
            if i in set_seen:
                return True
            else:
                set_seen.add(i)
        return False