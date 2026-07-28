class TrieNode {
public:
    // Move member variables out of the constructor scope so they dont die once constrcutor finishes
    unordered_map<char, TrieNode*> children;
    bool endOfWord = false;

    TrieNode() = default;
};

class PrefixTree {
public:
    TrieNode* root = new TrieNode();
    
    PrefixTree() = default;
    
    void insert(string word) {
        TrieNode* curr = root;
        for (char ch : word) {
            if (!curr->children.contains(ch)) {
                curr->children[ch] = new TrieNode();
            }
            curr = curr->children[ch];
        }
        curr->endOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        for (char ch : word) {
            if (!curr->children.contains(ch)) {
                return false;
            }
            curr = curr->children[ch];
        }
        return curr->endOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char ch : prefix) {
            if (!curr->children.contains(ch)) {
                return false;
            }
            curr = curr->children[ch];
        }   
        return true;
    }
};

