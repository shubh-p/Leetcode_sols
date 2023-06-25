class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range(len(startTime)):
            if queryTime<=endTime[i] and queryTime>=startTime[i]:
                count+=1
        return count
        