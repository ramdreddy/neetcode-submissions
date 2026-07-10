class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ans;
        for(int i = 0; i < nums.size(); i++){
            int x = nums[i];
            int comp = target - x;
            if(ans.count(comp)){
                return {ans[comp] , i};
            }
            ans[x] = i;
        }
    }
};
