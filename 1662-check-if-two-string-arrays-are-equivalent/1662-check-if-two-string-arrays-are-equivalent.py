class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        s2=""
        for x in word1:
            s1+=x
        for x in word2:
            s2+=x
        if s1 == s2:
            return True
        else:
            return False