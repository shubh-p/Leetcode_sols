class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=defaultdict(int)
        loosers=defaultdict(int)
        ans=[]
        nolosses,onelosses=[],[]
        for pair in matches:
            winners[pair[0]]+=1
            loosers[pair[1]]+=1
        for player in winners:
            if player not in loosers:
                nolosses.append(player)
        ans.append(sorted(nolosses))
        for player in loosers:
            if loosers[player]==1:
                onelosses.append(player)
        ans.append(sorted(onelosses))
        
        return ans