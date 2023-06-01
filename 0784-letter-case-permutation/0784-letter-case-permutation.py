class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        def fn(ip,op):
            if len(ip)==0:
                ans.append(op)
                return
            c=ip[0]
            ip=ip[1:]
            if ord(c)<=ord('9') and ord(c)>=ord('0'):
                opx=op+c
                fn(ip,opx)
                return
            op1=op+c.lower()
            op2=op+c.upper()
            fn(ip,op1)
            fn(ip,op2)
            # return 
        fn(s,"")
        return ans