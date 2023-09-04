#User function Template for python3
class Solution:
    def minDifference(self, arr, n):
        total = sum(arr)
        dp = [[False for i in range(total + 1)] for j in range(n + 1)]

        for i in range(n + 1):
            for j in range(total + 1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True

        for i in range(1, n + 1):
            for j in range(1, total + 1):
                dp[i][j] = dp[i - 1][j]
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

        # Find the minimum absolute difference
        half_total = total // 2
        for j in range(half_total, -1, -1):
            if dp[n][j]:
                return total - 2 * j
	   # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends