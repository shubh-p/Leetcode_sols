class Solution:
    def minimumSum(self, num: int) -> int:
        string=str(num)
        a=[]
        a.append(string[0])
        a.append(string[1])
        a.append(string[2])
        a.append(string[3])
        a.sort()
        ans=(int(a[0])+int(a[1]))*10 + int(a[2]) + int(a[3])
        return ans