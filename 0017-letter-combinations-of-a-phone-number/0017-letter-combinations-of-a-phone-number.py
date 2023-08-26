class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        mapping={}
        mapping["2"]=["a","b","c"]
        mapping["3"]=["d","e","f"]
        mapping["4"]=["g","h","i"]
        mapping["5"]=["j","k","l"]
        mapping["6"]=["m","n","o"]
        mapping["7"]=["p","q","r","s"]
        mapping["8"]=["t","u","v"]
        mapping["9"]=["w","x","y","z"]
        # print(mapping)
        ans=[]
        def rec(comb,digits):
            if len(digits)==0:
                ans.append(comb)
                return 
            for c in mapping[digits[0]]:
                comb+=c
                rec(comb,digits[1:])
                comb=comb[:-1]
        rec("",digits)
        return ans