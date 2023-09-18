class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        ans=[]
        def rec(n,path):
            if n==0:
                nonlocal ans
                path.append(0)
                ans.append(path[::-1])
                path.remove(0)
                return
            for node,edge in enumerate(graph):
                if n in edge:
                    path.append(n)
                    rec(node,path)
                    path.remove(n)       
        rec(n-1,[])
        return ans
