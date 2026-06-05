class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for char in s.lower():
            if char.isalnum():
                s1+=char
        if s1==s1[::-1]:
            return True
        else:
            return False