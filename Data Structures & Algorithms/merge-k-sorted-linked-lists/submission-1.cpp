/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    struct compare {    //max heap into minheap
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val;
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, compare> pointers;
        for (ListNode* head : lists) {
            if (head) {
                pointers.push(head);
            }
        }

        ListNode dummy(0);
        ListNode* curr = &dummy;

        while (!pointers.empty()) {
            ListNode* smallest = pointers.top();
            pointers.pop();

            curr->next = smallest;
            curr = curr->next;

            if (smallest->next) {
                pointers.push(smallest->next);
            }
        }
        return dummy.next;
    }
};
