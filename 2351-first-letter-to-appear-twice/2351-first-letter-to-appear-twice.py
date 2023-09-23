class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a= list(s)
        x=[0]*26
        for c in a:
            if x[ord(c)- 97]==0:
                
                x[ord(c)-97]+=1
            else:
                
                return c
        
        
        