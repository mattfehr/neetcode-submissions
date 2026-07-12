/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head: ListNode | null): void {
        let slow = head, fast = head;
        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;
        }
        let prev = null, curr = slow.next;
        slow.next = null;
        while (curr) {
            let nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        let l1 = head, l2 = prev;
        while (l1 && l2) {
            let nxt1 = l1.next, nxt2 = l2.next;
            l1.next = l2;
            l2.next = nxt1;
            l1 = nxt1;
            l2 = nxt2;
        }
    }
}
