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
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists) {
        if (!lists || lists.length === 0) return null;
        
        let k = lists.length;
        while (k > 1) {
            for (let i = 0; i < Math.floor(k / 2); i++) {
                // Pairwise merge from both ends of the active list range
                lists[i] = this.mergeTwoLists(lists[i], lists[k - 1 - i]);
            }
            // Halve the active size for the next round
            k = Math.ceil(k / 2);
        }
        
        return lists[0];
    }

    /**
     * Helper method to merge two sorted lists
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    mergeTwoLists(l1, l2) {
        const dummy = new ListNode(0);
        let current = dummy;
        
        while (l1 !== null && l2 !== null) {
            if (l1.val < l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }
        
        // Link remaining nodes
        current.next = l1 !== null ? l1 : l2;
        
        return dummy.next;
    }
}
