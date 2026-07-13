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
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head: ListNode | null, n: number): ListNode {
        let curr = head;
        let count = 0;
        while (curr) {
            count += 1;
            curr = curr.next;
        }
        const target = count-n;
        const dummy = new ListNode(0, head);
        curr = dummy;
        for (let i = 0; i < target; ++i) {
            curr = curr.next;
        }
        if (curr.next && curr.next.next) {
            curr.next = curr.next.next;
        } else {
            curr.next = null;
        }
        return dummy.next;
    }
}
