class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x=0;
        int n=operations.size();
        for(int i=0;i<n;i++)
        {
            if(operations[i]=="++X" || operations[i] == "X++")
            {
                x++;
            }
            else
                x--;
        }
        return x;
    }
};