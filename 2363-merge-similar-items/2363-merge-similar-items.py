class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        a={}
        for item in items1:
            a[item[0]]=item[1]
        for item in items2:
            if item[0] in a:
                a[item[0]] += item[1]
            else:
                a[item[0]]=item[1]
        x=sorted(a)
        ans=[]
        for key in x:
            ans.append([key,a[key]])
        return ans
