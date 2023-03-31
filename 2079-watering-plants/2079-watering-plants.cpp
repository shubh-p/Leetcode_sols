class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int can=capacity;
        int n=plants.size();
        int steps=1,tofro;
        for(int i=0;i<n-1;i++)
        {
            can=can-plants[i];
           
            if(can<plants[i+1])
            {
                tofro=2*(i+1);
                
                steps=steps+tofro;
                can=capacity;
            }
            steps++;
        }
        
        return steps;
        
    }
};