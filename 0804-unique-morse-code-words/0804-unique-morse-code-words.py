class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        se=set()
        
        for s in words:
            x=""
            for i in s:
                x+=a[ord(i)-97]
            se.add(x)
        return len(se)
            