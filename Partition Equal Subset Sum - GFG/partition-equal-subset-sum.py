# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        n=N
        total=sum(arr)
        if total%2==1:
            return False
        memo=[[-1 for i in range(total+1)]for j in range(n+1)]
        def rec(n,sum):
            if memo[n][sum]!=-1:
                return memo[n][sum]
            if n==0:
                if 2*sum==total:
                    memo[0][sum]=True
                    return True
                else:
                    memo[0][sum]=False
                    return False
            t= rec(n-1,sum+arr[n-1]) or rec(n-1,sum)
            memo[n][sum]=t
            return t
        return rec(n,0)
        # code here
    

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends