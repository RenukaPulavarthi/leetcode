class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
         vector<vector<int>> ans;
         map<vector<int>,int>m;
         sort(nums.begin(),nums.end());
         for(int i=0;i<nums.size();i++)
         {
            int x=i+1;
            int y=nums.size()-1;
            while(x<y)
            {
                int w=nums[i]+nums[x]+nums[y];
                if (w==0)
                {
                    vector<int>t={nums[i],nums[x],nums[y]};
                    if(m[t]==0){
                        ans.push_back(t);
                        m[t]+=1;
                    }
                    x++;
                }
                else if(w>0) y--;
                else x++;
            }
         }
         return ans;
    }
};