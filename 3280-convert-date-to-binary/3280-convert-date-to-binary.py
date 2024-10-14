class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums=date.split('-')
        res=[]
        for num in nums:
            binary=bin(int(num))
            res.append(binary[2:])
        return "-".join(res)