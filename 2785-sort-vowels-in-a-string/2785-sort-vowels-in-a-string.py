class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels=['a','e','i','o','u','A','E','I','O','U']
        va=[]
        ca=[]
        res=[]
        for chars in s:
            if chars in vowels:
                va.append(chars)
                res.append("v")
            else:
                ca.append(chars)
                res.append("c")
        va.sort()
        for i,c in enumerate(res):
            if c=="v":
                res[i]=va.pop(0)
            else:
                res[i]=ca.pop(0)
        
        return "".join(res)
                
        