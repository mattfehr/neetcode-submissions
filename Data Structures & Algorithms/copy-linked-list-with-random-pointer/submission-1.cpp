/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> oldToCopy;
        oldToCopy[nullptr] = nullptr;

        Node* curr = head;
        while (curr != nullptr) {
            //node doesnt exist in dict, need to create
            if (oldToCopy.find(curr) == oldToCopy.end()) {
                oldToCopy[curr] = new Node(0);
            }
            oldToCopy[curr]->val = curr->val;

            //next node doesnt exsit
            if (oldToCopy.find(curr->next) == oldToCopy.end()) {
                oldToCopy[curr->next] = new Node(0);
            }
            oldToCopy[curr]->next = oldToCopy[curr->next];

            //random node hasnt been made yet
            if (oldToCopy.find(curr->random) == oldToCopy.end()) {
                oldToCopy[curr->random] = new Node(0);
            }
            oldToCopy[curr]->random = oldToCopy[curr->random];

            curr = curr->next;
        }
        return oldToCopy[head];
    }
};
