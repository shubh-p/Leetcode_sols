class Solution:
    def minTimeToType(self, word: str) -> int:
        def fn(curr: chr, to: chr) -> int:
            clockwise=abs(ord(to)-ord(curr))
            anticlockwise=26-clockwise
            if clockwise<=anticlockwise:
                return clockwise
            elif anticlockwise<clockwise:
                return anticlockwise
        curr='a'
        ans=0
        for c in word:
            
            steps=fn(curr,c)
            ans+=steps
            curr=c
            print(steps)
        return ans+len(word)

