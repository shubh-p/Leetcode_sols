class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        box=list(boxes)
        print(box)
        ans=[]
        for i in range(len(box)):
            sum=0
            for j in range(len(box)):
                if box[j]=='1':
                    sum+=abs(i-j)
            ans.append(sum)
        return ans