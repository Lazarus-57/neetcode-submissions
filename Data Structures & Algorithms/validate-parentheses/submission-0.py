class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        reference={")":"(","]":"[","}":"{"}
        for char in s:
            if char in reference:
                if stack and stack[-1]==reference[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

            

            