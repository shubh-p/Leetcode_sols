class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        pair={}
        ans=[]
        x=97
        for a in key:
            if a in pair:
                continue
            elif a ==' ':
                continue
            else:
                pair[a]=chr(x)
                x+=1
        for a in message:
            if a == ' ':
                ans.append(' ')
            else:
                ans.append(pair[a])
        return "".join(ans)
                    