class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1=Counter(word1)
        c2=Counter(word2)
        # print(c1,c2)
        # print(set(c1.values()),set(c2.values()))
        # print(set(c1.keys()),(set(c2.keys())))
        # print(set(c1.values()).difference(set(c2.values())))
        # return len(set(c1.keys()).difference(set(c2.keys())))==0 and len(set(c1.values()).difference(set(c2.values())))==0
        a=sorted(c1.keys())
        b=sorted(c2.keys())
        c=sorted(c1.values())
        d=sorted(c2.values())
        # print(a,b,c,d)
        return a==b and c==d
        