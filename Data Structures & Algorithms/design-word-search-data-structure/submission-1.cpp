class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool endOfWord = false;
    TrieNode() = default;
};

class WordDictionary {
public:
    TrieNode* root = new TrieNode();
    WordDictionary() = default;

    void addWord(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children[c] == nullptr) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->endOfWord = true;
    }

    bool search(string word) {
        return dfs(0, this->root, word);
    }

    // Fixed DFS logic using tracking variable 'i'
    bool dfs(int i, TrieNode* curr, const string& word) {
        if (curr == nullptr) return false;
        
        // Base case: we processed the whole word
        if (i == word.size()) {
            return curr->endOfWord;
        }

        if (word[i] == '.') {
            // Wildcard: try all possible matching child paths
            for (auto& [key, value] : curr->children) {
                if (dfs(i + 1, value, word)) {
                    return true;
                }
            }
            return false;
        } else {
            // Exact character matching
            if (curr->children.find(word[i]) == curr->children.end()) {
                return false;
            }
            return dfs(i + 1, curr->children[word[i]], word);
        }
    }
};
