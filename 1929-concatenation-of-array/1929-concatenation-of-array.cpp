class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int length=nums.size();
        for(int i=0;i< 2*length; i++)
            {
                if(i<length)
                {
                    ans.push_back(nums.at(i));
                }
                else
                {
                    ans.push_back(nums.at(i-length));
                }
            }
        return ans;
    }
};