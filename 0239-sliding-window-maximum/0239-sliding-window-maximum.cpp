class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int>que;
        vector<int>ans;
        for(int i=0;i<k;i++){
            while(!que.empty() && que.back()<nums[i]){
                que.pop_back();
            }
            que.push_back(nums[i]);
        }
        ans.push_back(que.front());
        for(int i=k;i<nums.size();i++){
            while(!que.empty() && que.back()<nums[i]){
                que.pop_back();
            }
            que.push_back(nums[i]);
            if(que.front()==nums[i-k]){
                que.pop_front();
            }
            ans.push_back(que.front());
        }
        return ans;
    }
};