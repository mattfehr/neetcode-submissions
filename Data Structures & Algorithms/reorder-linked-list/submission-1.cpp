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
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* prev = nullptr;
        ListNode* curr = slow->next;
        slow->next = nullptr;
        while (curr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }
        ListNode* l1  = head;
        ListNode* l2 = prev;
        while (l1 && l2) {
            ListNode* temp1  = l1->next;
            ListNode* temp2 = l2->next;
            l1->next = l2;
            l2->next = temp1;
            l1 = temp1;
            l2=temp2;
        }
    }
};
