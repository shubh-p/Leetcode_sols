class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans;
        int length=nums.size();
        for(int i=0;i<length;i++)
        {
            ans.push_back(nums.at(nums.at(i)));
        }
        return ans;
    }
};