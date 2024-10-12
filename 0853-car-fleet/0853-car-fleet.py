class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic={}
        stack=[]
        for i in range(len(position)):
            dic[position[i]]=((target-position[i])/speed[i])
        times=list(dict(sorted(dic.items())).values())
        for time in times:
            while len(stack)>0 and time>=stack[-1]:
                stack.pop(-1)
            stack.append(time)
        return len(stack)