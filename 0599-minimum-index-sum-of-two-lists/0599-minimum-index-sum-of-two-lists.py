class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a={}
        ans=[]
        for i,x in enumerate(list1):
            a[x]=i
        m=len(list1)+len(list2)-2
        for i,x in enumerate(list2):
            if x in a:
                if i+a[x]<m:
                    m=i+a[x]
        for i,x in enumerate(list2):
            if x in a and i+a[x]==m:
                ans.append(x)
        return ans