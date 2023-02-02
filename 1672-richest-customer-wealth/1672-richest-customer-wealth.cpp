class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int m=accounts.size();
        int maxsum=INT_MIN,sum;
        for(int i=0;i<m;i++)
        {
            sum=0;
            for(int j=0;j<accounts[i].size();j++)
            {
                sum+=accounts[i][j];
            }
            maxsum=max(maxsum,sum);
        }
        return maxsum;
    }
};