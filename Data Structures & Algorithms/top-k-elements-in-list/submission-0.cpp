class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> final;
        unordered_map<int, int> ans;
        for(int x : nums){
            ans[x]++;
        }
        vector<vector<int>> buckets(nums.size()+1);
        for(auto[num, freq]: ans){
            buckets[freq].push_back(num);
        }
        for(int i = buckets.size()-1; i >= 0; i--){
           for(int x : buckets[i]){
            final.push_back(x);
           }
           if(final.size() == k){
            return final;
           }
        }
        return final;
    }
};
