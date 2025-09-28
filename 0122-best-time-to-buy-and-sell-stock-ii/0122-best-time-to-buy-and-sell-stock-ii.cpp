class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans=0;
        int l=prices.size();
        for(int i=0;i<l-1;i++){
            if(prices[i]<prices[i+1]){
                ans+=(prices[i+1]-prices[i]);
            }
        }
        return ans;
    }
};