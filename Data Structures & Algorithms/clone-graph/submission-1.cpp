#include <unordered_map>
#include <queue>
#include <vector>

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) {
            return nullptr;
        }
        
        // Maps original node pointers to their cloned node pointers
        std::unordered_map<Node*, Node*> old_to_new;
        
        // Clone the root node and add to map
        old_to_new[node] = new Node(node->val);
        
        std::queue<Node*> q;
        q.push(node);
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            
            for (Node* neighbor : curr->neighbors) {
                // If neighbor hasn't been cloned yet
                if (old_to_new.find(neighbor) == old_to_new.end()) {
                    old_to_new[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                
                // Link the clone's neighbor using the map
                old_to_new[curr]->neighbors.push_back(old_to_new[neighbor]);
            }
        }
        
        return old_to_new[node];
    }
};
