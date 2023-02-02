class Solution {
public:
    bool isPalindrome(int x) {
        vector<int> nums;
        int k=x;
        int temp;
        if(k<0)
        {
            return false;
        }
        while(k!=0)
        {
            temp=k%10;
            nums.push_back(temp);
            k=k/10;
        }
        /*for(int i=0;i<nums.size();i++)
        {
            cout<<nums[i];
        }*/
        int l=nums.size();
       
        for(int i=0;i<l/2;i++)
        {
            if(nums[i]!=nums[l-i-1])
            {
              return false;  
            }
            
        }
        return true;
    }
        
    
        
};