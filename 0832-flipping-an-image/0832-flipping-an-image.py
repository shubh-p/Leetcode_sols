class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i=0
            j=len(row) - 1
            while(i<=j):
                if i==j:
                    row[i]=1-row[i]
                elif row[i]==row[j]:
                    row[i]=1-row[i]
                    row[j]=1-row[j]
                i+=1
                j-=1
        return image