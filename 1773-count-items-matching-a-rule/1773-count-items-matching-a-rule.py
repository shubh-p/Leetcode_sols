class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            x=0
        elif ruleKey == "color":
            x=1
        elif ruleKey == "name":
            x=2
        count=0
        for item in items:
            if item[x]==ruleValue:
                count+=1
        return count
            