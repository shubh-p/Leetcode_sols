class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans=[]
        for person,gs in enumerate(groupSizes):
            temp=[]
            if gs==0:
                continue
            elif gs==1:
                temp.append(person)
            else:
                temp.append(person)
                thisgroup=gs
                groupSizes[person]=0
                for i in range(gs-1):  
                    ind=groupSizes.index(thisgroup)
                    temp.append(ind)  
                    groupSizes[ind]=0         
            ans.append(temp)
        return ans
