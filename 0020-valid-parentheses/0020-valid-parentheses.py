class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair = {
           ")":"(",
           "]":"[",
           "}":"{"
                    }
        stack.append("-1")
        for c in s:
            if c in ["(","[","{"]:
                stack.append(c)
            elif stack[-1]==pair[c]:
                stack.pop()
            else:
                return False
        if len(stack)==1:
            return True
        return False