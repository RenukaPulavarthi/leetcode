class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        map<long long,long long>prev;
        map<long long,long long>next;
        int mod=1000000007;
        for(auto it:nums){
            next[it]++;
        }
        long long ans=0;
        prev[nums[0]]++;
        next[nums[0]]--;
        for(int i=1;i<nums.size();i++){
            next[nums[i]]--;
            if(prev.find(nums[i]*2)!=prev.end() && next.find(nums[i]*2)!=next.end()){
                long long k=((prev[nums[i]*2]%mod)*(next[nums[i]*2]%mod))%mod;
                ans+=k;
                ans=ans%mod;
            }
            prev[nums[i]]++;
        }
        return (int)ans;
    }
};