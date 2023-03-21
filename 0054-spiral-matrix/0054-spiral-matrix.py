class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        ans=[]
        top,down,left,right=0,m-1,0,n-1
        
        while top<=down and left<= right:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,down+1):
                ans.append(matrix[i][right])
            right-=1
            if top<=down:
                for i in range(right,left-1,-1):
                    ans.append(matrix[down][i])
            down-=1
            if left<=right:
                for i in range(down,top-1,-1):
                    ans.append(matrix[i][left])
            left+=1
        return ans