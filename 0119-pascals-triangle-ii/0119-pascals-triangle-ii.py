class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo={}
        def factorial(n:int,memo) -> int:   
            if n==0:
                return 1
            elif n in memo.keys():
                return memo[n]
            else:
                ans=n*factorial(n-1,memo)
                #print("call")
                memo[n]=ans
                return ans
        result=[]
        for i in range(rowIndex+1):
            result.append(factorial(rowIndex,memo)//(factorial(i,memo)*factorial(rowIndex-i,memo)))
        return result