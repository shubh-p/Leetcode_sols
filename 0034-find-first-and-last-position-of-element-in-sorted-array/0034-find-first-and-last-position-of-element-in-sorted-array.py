class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # def bs(i,j,target,a):
        #     while i<=j:
        #         mid=(i+j)//2
        #         if a[mid]>target:
        #             j=mid-1
        #         elif a[mid]<target:
        #             i=mid+1
        #         else:
        #             return mid
                
        #     return -1

        
        # # print(bs(0,len(nums)-1,target,nums))
        # def rec(i,j,target,start,end,pos,a):
        #     pos=bs(i,j,target,a)
            
        # return []
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2  # Calculate the middle index

                if arr[mid] == target:
                    return mid  # Found the target, return its index
                elif arr[mid] < target:
                    left = mid + 1  # Target is in the right half
                else:
                    right = mid - 1  # Target is in the left half

            return -1
        if binary_search(nums,target)==-1:
            return [-1,-1]
        lower_bound = bisect.bisect_left(nums, target)
        upper_bound = bisect.bisect_right(nums, target)
        return [lower_bound, upper_bound-1]