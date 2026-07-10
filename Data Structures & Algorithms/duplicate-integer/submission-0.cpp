class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> ans;
        for(int x : nums){
            ans[x]++;
        }
        for(auto[key,val] : ans){
            if (val>1 ){
                return true;
            }
        }
        return false;
    }
};