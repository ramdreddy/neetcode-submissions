class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        map<vector<int>, vector<string>> prob;
        for(string s : strs){
            vector<int> counts(26, 0);
            for(char c : s){
                counts[c - 'a']++;
            }
            prob[counts].push_back(s);
        }
        for(auto[key, val]: prob){
            ans.push_back(val);
        }
        return ans;
    }
};
