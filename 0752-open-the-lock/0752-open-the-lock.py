class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        Deadends=set(deadends)
        Deadends.add("0000")
        q=collections.deque()
        q.append("0000")
        def children(lock):
            ans=[]
            for i in range(4):
                ans.append(lock[:i]+str((int(lock[i])+1)%10)+lock[i+1:])
                ans.append(lock[:i]+str((int(lock[i])+9)%10)+lock[i+1:])      
            return ans
        steps=0
        while q:
            # print(q,step)
            # print(q,steps)
            for i in range(len(q)):
                c=q.popleft()
                if c==target:
                    return steps                
                # Deadends.add(c)
                for child in children(c):
                    if child not in Deadends:
                        q.append(child)
                        Deadends.add(child)
            steps+=1
        # print(Deadends)
        return -1	
        