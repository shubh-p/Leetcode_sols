#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        memo = [[-1 for i in range(W + 1)] for i in range(n + 1)]
        
        def rec(w, n):
            if w == 0 or n == 0:
                return 0
            if memo[n][w] != -1:
                return memo[n][w]   
            if wt[n - 1] <= w:
                memo[n][w] = max(val[n - 1] + rec(w - wt[n - 1], n - 1), rec(w, n - 1))
                return memo[n][w]
            else:
                memo[n][w] = rec(w, n - 1)
                return memo[n][w]
        
        return rec(W, n)
       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends