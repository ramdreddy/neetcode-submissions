class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size(), 1);
        int val = 1;
        for(int i = 0; i < nums.size(); i++){
            ans[i] = val;
            val*=nums[i];
        }
        int val2 = 1;
        for(int i = nums.size()-1; i >= 0; i--){
            ans[i]*=val2;
            val2*=nums[i];
        }
        return ans;
    }
};
