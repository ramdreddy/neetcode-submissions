class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> ans;
        int count = 1;
        int prev = 0;
        ans.insert(nums.begin(), nums.end());
        for(int x : ans){
            if (ans.count(x+1)){
                count = 2;
                while(ans.count(count+x)){
                    count++;
                }
            }
            prev = max(prev, count);
        }
        return prev;
    }
};
