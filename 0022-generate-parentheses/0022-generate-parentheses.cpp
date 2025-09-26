class Solution {
public:
    vector<string> Solve(string s,int open,int closed,int n,vector<string>& ans){
        if(open+closed>=n*2){
            ans.push_back(s);
            return ans;
        }
        if(closed>open){
            return ans;
        }
        if(open==n){
            Solve(s+')',open,closed+1,n,ans);
        }
        else{
            Solve(s+'(',open+1,closed,n,ans);
            Solve(s+')',open,closed+1,n,ans);
        }
        return ans;
    }
    vector<string> generateParenthesis(int n) {
        vector<string> s;
        return Solve("(",1,0,n,s);
    }
};