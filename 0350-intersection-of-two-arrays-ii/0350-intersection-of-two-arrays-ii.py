class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a,b={},{}
        ans=[]
        for num in nums1:
            a[num]=1+a.get(num,0)
        for num in nums2:
            b[num]=1+b.get(num,0)
        if len(a)<=len(b):
            for i in a:
                if i in b:
                    m=min(a[i],b[i])
                    ans+=[i]*m
        else:
             for i in b:
                if i in a:
                    m=min(a[i],b[i])
                    ans+=[i]*m
        return ans