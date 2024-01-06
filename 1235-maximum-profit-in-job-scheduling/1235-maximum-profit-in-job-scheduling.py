from typing import List
import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        sorted_end_times = [x[1] for x in jobs]
        n = len(jobs)
        
        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            current_start, _, current_profit = jobs[i]
            # Find the latest job that finishes before the current job starts
            j = bisect.bisect_right(sorted_end_times, current_start) - 1
            if j >= 0:
                current_profit += dp[j]
                
            dp[i] = max(current_profit, dp[i - 1])

        return dp[-1]