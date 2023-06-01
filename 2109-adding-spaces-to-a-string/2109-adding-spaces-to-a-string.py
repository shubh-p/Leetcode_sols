class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        anss=""
        j=0
        spaces.append(len(s))
        # print(spaces)
        for i in range(len(s)):
            if j==len(spaces):
                break
            if i<spaces[j]:
                anss+=s[i]
            else:
                anss+=" "
                anss+=s[i]
                j+=1
        return anss