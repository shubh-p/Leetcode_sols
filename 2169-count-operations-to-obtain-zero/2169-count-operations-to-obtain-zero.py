class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count=0
        if num1==0 or num2==0:
            return 0
        while(True):
            if num1>=num2:
                num1-=num2
            elif num2>=num1:
                num2-=num1
            count+=1
            if num1==0 or num2==0:
                break
        return count
        