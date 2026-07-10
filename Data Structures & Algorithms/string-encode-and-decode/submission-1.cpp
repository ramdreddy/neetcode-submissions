class Solution {
public:

    string encode(vector<string>& strs) {
        string ans;
        for(string &s : strs){
            string size = to_string(s.size());
            ans +=  size + '&' + s;
        }
        return ans;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        int i = 0;
        while(i < s.size()){
            int dis = s.find('&', i);
            string length = s.substr(i, dis - i);
            int len = stoi(length);
            ans.push_back(s.substr(dis+1, len));
            i = dis + len + 1;
        }
        return ans;
    }
};
