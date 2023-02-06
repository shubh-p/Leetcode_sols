SECOND TRY O(n)
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
      
      
      
FIRST TRY O(n^2)
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
