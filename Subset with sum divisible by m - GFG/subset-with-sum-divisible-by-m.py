#User function Template for python3

class Solution:
	def DivisibleByM(self, nums, m):
		# Code here
        
        def rec(n,sum):
            if n==0 :
                if sum !=0 and sum%m==0:
                    # print(sum)
                    return True
                else:
                    return False
                
            
            return rec(n-1,sum+nums[n-1]) or rec(n-1,sum)
            
        ans=rec(len(nums),0)
        
        return 1 if ans else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split();
		n = int(n);
		m = int(m);
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.DivisibleByM(nums, m)
		print(ans)
# } Driver Code Ends