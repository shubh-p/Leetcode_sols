class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def apsum(num,a):
            return num*a/2*(1+num)
        def count(num):
            return n//num
        threes=count(3)
        fives=count(5)
        sevens=count(7)
        fifteens=count(15)
        twentyones=count(21)
        thirtyfives=count(35)
        hundredfives=count(105)
        ans=apsum(threes,3)+apsum(fives,5)+apsum(sevens,7)-apsum(fifteens,15)-apsum(twentyones,21)-apsum(thirtyfives,35)+apsum(hundredfives,105)
        return int(ans)

        
        