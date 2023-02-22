class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        a=[0]*26
        for s in sentence:
            a[ord(s)-ord('a')]=1
            if sum(a)==26:
                return True
        return False