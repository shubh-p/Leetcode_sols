class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ans=list(s)
        begin=0
        for pos,i in enumerate(s):
            if i=="(":
                stack.append(1)
            elif i==")":
                stack.pop()
            if len(stack)==0:
                ans[begin]=""
                ans[pos]=""
                begin=pos+1
        
        return "".join(ans)
