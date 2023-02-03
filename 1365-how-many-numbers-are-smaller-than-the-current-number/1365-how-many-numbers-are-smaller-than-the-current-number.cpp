// o(n2)
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int n=nums.size();
        int num,count;
        vector <int> a;
        for(int i=0;i<n;i++)
        {
            num=nums[i];
            count=0;
            for(int j=0;j<n;j++)
            {
                if((i!=j) && (nums[j]<nums[i]))
                    count++;
            }
            a.push_back(count);
        }
        return a;
    }
};