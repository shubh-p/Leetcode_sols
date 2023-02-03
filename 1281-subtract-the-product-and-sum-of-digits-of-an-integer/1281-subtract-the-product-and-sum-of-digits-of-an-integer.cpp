class Solution {
public:
    int subtractProductAndSum(int n) {
        int product=1,sum=0,digit;
        while(n>0)
        {
            digit=n%10;
            sum+=digit;
            product*=digit;
            n/=10;
        }
        return (product-sum);
    }
};