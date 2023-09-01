#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        
        memo=[[None for j in range(sum+1)]for i in range(N+1)]
        # print(memo)
        for i in range(N+1):
            for j in range(sum+1):
                if i==0:
                    memo[i][j]=False
                if j==0:
                    memo[i][j]=True
        # print(memo)
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    memo[i][j]=memo[i-1][j-arr[i-1]] or memo[i-1][j]
                else:
                    memo[i][j]=memo[i-1][j]
        if memo[N][sum]:
            return 1
        else:
            return False
        
        # memo=[[None for i in range(sum+1)]for j in range(N+1)]
        # def rec(n,sum):
        #     if memo[n][sum]!=None:
        #         return memo[n][sum]
        #     if sum==0:
        #         memo[n][sum]= True
        #         return True
        #     if n==0:
        #         memo[n][sum]= False
        #         return False
        #     if arr[n-1]<=sum:
        #         memo[n][sum]= rec(n-1,sum-arr[n-1]) or rec(n-1,sum)
        #         return memo[n][sum]
        #     else:
        #         memo[n][sum]= rec(n-1,sum)
        #         return memo[n][sum]
        
        # ans=rec(N,sum)
        # return 1 if ans is True else 0
        
        
        


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