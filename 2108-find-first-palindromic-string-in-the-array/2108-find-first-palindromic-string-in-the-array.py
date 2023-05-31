class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def check(a:str) -> bool:
            i,j=0,len(a) - 1
            while(i<j):
                if a[i] != a[j]:
                    return False
                i+=1
                j-=1
            return True
        for word in words:
            if len(word) == 1:
                return word
            elif check(word):
                return word
        return ""