#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        memo=[[None for i in range(sum+1)]for j in range(N+1)]
        # print(memo)
        def rec(n,sum):
            if memo[n][sum]!=None:
                return memo[n][sum]
            if sum==0:
                memo[n][sum]= True
                return True
            if n==0:
                memo[n][sum]= False
                return False
            if arr[n-1]<=sum:
                memo[n][sum]= rec(n-1,sum-arr[n-1]) or rec(n-1,sum)
                return memo[n][sum]
            else:
                memo[n][sum]= rec(n-1,sum)
                return memo[n][sum]
        
        ans=rec(N,sum)
        return 1 if ans is True else 0
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends