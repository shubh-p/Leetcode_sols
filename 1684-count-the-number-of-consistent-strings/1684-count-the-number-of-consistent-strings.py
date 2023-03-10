class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        a=allowed
        flag=0
        for s in words:
            for i in s:
                if i in a:
                    flag=1
                else:
                    flag=0
                    break
            if flag == 1:
                count+=1
        return count
        