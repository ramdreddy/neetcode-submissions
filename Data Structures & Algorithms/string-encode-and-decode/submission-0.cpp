class Solution {
public:

    string encode(vector<string>& strs) {
        string out;
        for(string s : strs){
            string size = to_string(s.size());
            out += size + "#" + s;
        }
        return out;
    }

    vector<string> decode(string s) {
        vector<string> final;
        int i = 0;
        while(i < s.size()){
            int j = s.find('#', i);
            int size = stoi(s.substr(i, j-i));
            string ans = s.substr(j+1, size);
            final.push_back(ans);
            i = j + size+1;
        }
        return final;
    }
};
