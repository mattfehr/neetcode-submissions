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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* curr = head;
        int count = 0;
        while (curr) {
            count++;
            curr = curr->next;
        }
        int target = count-n;
        ListNode* dummy = new ListNode(0, head);
        curr = dummy; 
        for (int i = 0; i < target; ++i) {
            curr = curr->next;
        }
        if (curr->next && curr->next->next) {
            curr->next = curr->next->next;
        } else {
            curr->next = nullptr;
        }
        return dummy->next;
    }
};
