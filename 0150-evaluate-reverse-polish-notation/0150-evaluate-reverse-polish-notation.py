class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=set(["+","-","*","/"])
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                a=stack.pop(-1)
                b=stack.pop(-1)
                res=int(eval(b+token+a))
                stack.append(str(res))   
        return int(stack[0])
