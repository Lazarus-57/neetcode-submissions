class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1=list(s)
        list2=list(t)
        if sorted(list1)==sorted(list2):
            return True
        else:
            return False