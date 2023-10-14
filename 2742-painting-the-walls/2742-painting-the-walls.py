from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        memo = {}  # Dictionary to store computed results

        def rec(i, remaining):
            if remaining <= 0:
                return 0
            if i >= len(cost):
                return float("inf")

            # Check if the result for these parameters is already computed and stored
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            take = cost[i] + rec(i + 1, remaining - 1 - time[i])
            notake = rec(i + 1, remaining)

            # Store the result in the memo dictionary before returning
            memo[(i, remaining)] = min(take, notake)
            return memo[(i, remaining)]

        return rec(0, len(cost))
