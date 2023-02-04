class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        marks={}
        ans=[]
        for i,student in enumerate(score):
            marks[i]=student[k]
        marks=dict(sorted(marks.items(), key=lambda item: item[1],reverse=True))
                 #(kv[1], kv[0]))
        #print(marks)
        for i in marks.keys():
            ans.append(score[i])
        return ans