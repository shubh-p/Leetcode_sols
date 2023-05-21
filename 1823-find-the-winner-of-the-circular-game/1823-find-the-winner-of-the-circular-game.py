class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q=collections.deque(maxlen=n)
        for i in range(1,n+1):
            q.append(i)
        for i in range(1,n):
            q.rotate(1-k)
            q.popleft()
            # print(q)
        return q.popleft()