class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        box=list(boxes)
        pos=0
        count=0
        ans=[]
        for i in range(len(box)):
            if box[i]=='1':
                count+=1
                pos+=i
        ans.append(pos)
        for i in range(1,len(box)):
            c=boxes[0:i].count('1')
            ans.append(ans[i-1]+2*c-count)
        return ans
        