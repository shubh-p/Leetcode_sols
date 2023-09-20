class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        ans=[0 for i in range(n)]
        deck.sort()
        k=0
        for i in range(0,n,2):
            ans[i]=deck[k]
            k+=1
        print(ans)
        # i=0
        flag=False
        while k<n:
            i=i%n
            if ans[i]==0 and flag==True:
                ans[i]=deck[k]
                k+=1
                # i+=1
                flag=False
            elif ans[i]==0:
                flag=True
            i+=1
        return ans