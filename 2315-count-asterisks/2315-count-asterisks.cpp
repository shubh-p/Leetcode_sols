class Solution {
public:
    int countAsterisks(string s) {
        int length = s.length();
        cout<<length;
        int ans=0;
        int count=0;
        for(int i=0;i<length;i++)
        {
            if(s[i]=='|')
            {
                count++;
                
            }
            if(s[i]=='*' and count % 2 == 0)
            {
                ans++;
            }
        }
        
        return ans;
    }
};