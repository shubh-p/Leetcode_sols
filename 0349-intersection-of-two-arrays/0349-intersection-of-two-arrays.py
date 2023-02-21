class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        s1=set(nums1)
        s2=set(nums2)
        if len(s1)<=len(s2):
            for i in s1:
                if i in s2:
                    ans.append(i)
        else:
            for i in s2:
                if i in s1:
                    ans.append(i)
        return ans
        