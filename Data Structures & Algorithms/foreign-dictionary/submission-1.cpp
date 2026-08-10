class Solution {
public:
    string foreignDictionary(vector<string>& words) {
        unordered_map <char, unordered_set<char>> adjList;
        unordered_map <char, int> inDegree;

        for (string word : words) {
            for (char c : word) {
                if (!adjList.contains(c)) {
                    inDegree[c] = 0;
                }
            }
        }

        for (int i = 0; i < words.size()-1; ++i) {
            string word1 = words[i];
            string word2 = words[i+1];

            if (word1.size() > word2.size() && word1.starts_with(word2)) {
                return "";
            }

            int minLength = min(word1.size(), word2.size());
            for (int j = 0; j < minLength; ++j) {
                char char1 = word1[j];
                char char2 = word2[j];

                if (char1 != char2) {
                    if (!adjList[char1].contains(char2)) {
                        adjList[char1].insert(char2);
                        inDegree[char2]++;
                    }
                    break;
                }
            }
        }
        
        queue<char> q;
        for (const auto& [key, value] : inDegree)  {
            if (value == 0) {
                q.push(key);
            }
        }
        vector<char> sortedLetters;
        while (!q.empty()) {
            char currChar = q.front();
            q.pop();
            sortedLetters.push_back(currChar);

            for (char n : adjList[currChar]) {
                inDegree[n]--;
                if (inDegree[n] == 0) {
                    q.push(n);
                }
            }
        }

        if (sortedLetters.size() == inDegree.size()) {
            string sol = "";
            for (char c : sortedLetters) {
                sol += c;
            }
            return sol;
        } else {
            return "";
        }
    }
};
