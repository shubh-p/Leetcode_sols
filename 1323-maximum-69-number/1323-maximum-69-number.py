class Solution:
    def maximum69Number (self, num: int) -> int:
        na=str(num)
        n=list(na)
        for i in range(len(n)):
            if n[i]=="6":
                n[i]="9"
                break
        return int("".join(n))