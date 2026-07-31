#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool endOfWord = false;

    TrieNode() = default;
};

class Trie {
public:
    TrieNode* root = new TrieNode();

    void add(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (!curr->children.count(c)) { // Changed .contains to .count for universal compatibility
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->endOfWord = true;
    }
};

// Minimal addition: C++ needs a custom hash to use pairs in an unordered_set
struct pair_hash {
    size_t operator()(const pair<int, int>& p) const {
        return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
    }
};

class Solution {
private:
    Trie* trie = new Trie(); // Fixed: Must be a pointer because of 'new'
    unordered_set<pair<int, int>, pair_hash> seen; // Fixed: Added custom hash
    vector<pair<int, int>> dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}}; // Fixed: Changed [] to {}
    vector<string> sol;
    
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        for (string word : words) {
            this->trie->add(word); // Fixed: Uses -> instead of .
        }
        TrieNode* root = this->trie->root; // Fixed: Uses -> instead of .

        for (int r = 0; r < board.size(); ++r) {
            for (int c = 0; c < board[0].size(); ++c) {
                string current_word = ""; // Fixed: String needs an actual instance to be passed by reference
                dfs(r, c, root, current_word, board);
            }
        }
        return sol;
    }

    // Fixed: Added missing reference tokens (&) so board and word are not copied endlessly
    void dfs(int row, int col, TrieNode* curr, string &word, vector<vector<char>>& board) {
        char c = board[row][col]; // Fixed: Matrix indexing was missing [col]
        
        // Fixed: changed .search() to .count()
        if (!curr->children.count(c) || seen.count({row, col})) {
            return;
        }

        curr = curr->children[c];
        this->seen.insert({row, col}); // Fixed: changed () to {}
        word += c;
        if (curr->endOfWord) {
            this->sol.push_back(word);
            curr->endOfWord = false;
        }

        for (const auto& [dr, dc] : this->dirs) {
            int nr = row+dr, nc = col+dc;
            if (nr < 0 || nc < 0 || nr >= board.size() || nc >= board[0].size()) {
                continue;
            }
            dfs(nr, nc, curr, word, board); // Fixed: Passed board down to matches signature
        }

        this->seen.erase({row, col}); // Fixed: changed () to {}
        word.pop_back();
    }
};
