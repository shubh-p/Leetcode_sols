class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n=len(colors)
        if n<3:
            return False
        colors=list(colors)
        turn="A"
        i,j=1,1
        while i<n-1 and j<n-1:
            # print(colors,turn,i,j)
            if turn =="A":
                if colors[i-1]=="A" and colors[i+1]=="A" and colors[i]=="A":
                    colors.pop(i)
                    n-=1
                    turn="B"
                    if i>2:
                        i-=1
                    if j>2:
                        j-=1
                else:
                    i+=1
            elif turn =="B":
                if colors[j-1]=="B" and colors[j+1]=="B" and colors[j]=="B":
                    colors.pop(j)
                    n-=1
                    turn="A"
                    if i>2:
                        i-=1
                    if j>2:
                        j-=1
                else:
                    j+=1
            else:
                if turn=="A":
                    print("A's turn")
                    return False
                else:
                    return True
        print(colors)
        print(i,j)
        if i==n-1 and turn=="A":
            print("i reached end and it was A's turn ")
            return False
        elif j==n-1 and turn=="B":
            print("j reached end and it was B's turn ")
            return True