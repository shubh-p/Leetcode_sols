class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Merge sort top down using recursion
        def merge_sort(a):
            if len(a)<=1:
                return a
            mid=len(a)//2
            left_sub=merge_sort(a[0:mid])
            right_sub=merge_sort(a[mid:])
            return merge(left_sub,right_sub)

        def merge(l,r):
            i,j=0,0
            ans=[]
            while True:
                if l[i]<=r[j]:
                    ans.append(l[i])
                    i+=1
                else:
                    ans.append(r[j])
                    j+=1
                if i==len(l):
                    ans+=r[j:]
                    break
                elif j==len(r):
                    ans+=l[i:]
                    break
            return ans
        return merge_sort(nums)


