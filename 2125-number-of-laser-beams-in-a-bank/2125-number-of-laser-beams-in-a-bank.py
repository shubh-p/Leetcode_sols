class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        first=True
        for row in bank:
            count=row.count("1")
            if count>0 and first:
                first=False
                prev=count
            elif count>0:
                ans+=count*prev
                prev=count  
        return ans
            

        