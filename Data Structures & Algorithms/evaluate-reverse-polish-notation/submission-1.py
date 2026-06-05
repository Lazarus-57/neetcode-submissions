class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                v1=stack.pop()
                v2=stack.pop()
                ans=v2+v1
                stack.append(ans)
            elif i=="-":
                v1=stack.pop()
                v2=stack.pop()
                ans=v2-v1
                stack.append(ans)
            elif i=="*":
                v1=stack.pop()
                v2=stack.pop()
                ans=v2*v1
                stack.append(ans)
            elif i=="/":
                v1=stack.pop()
                v2=stack.pop()
                ans=int(v2/v1)
                stack.append(ans)
            else:
                stack.append(int(i))
        fin=stack.pop()
        return fin
