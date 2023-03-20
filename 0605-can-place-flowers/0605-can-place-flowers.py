class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        i=1
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                return True
            else:
                return False
        if len(flowerbed)==2:
            if n==2:
                return False
            if flowerbed[0]==1 or flowerbed[1]==1:
                return False
            return True
        flowerbed=[0]+flowerbed+[0]
        while i<len(flowerbed)-1:
            '''if flowerbed[0]==0 and flowerbed[1]==0:
                flowerbed[0]=1
                n-=1'''
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            if n==0:
                return True
            i+=1
        return False