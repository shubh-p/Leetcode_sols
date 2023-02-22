class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        temp=num
        if num<10:
            return 1
        while(num>0):
            digit=num%10
            if temp % digit ==0:
                print(digit)
                count+=1
            num=int(num/10)
        return count