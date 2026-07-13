/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        ListNode curr = head;
        int count = 0;
        while (curr is not null) {
            count += 1;
            curr = curr.next;
        }
        int target = count-n;
        ListNode dummy = new ListNode(0, head);
        curr = dummy;
        for (int i = 0; i < target; ++i) {
            curr = curr.next;
        }
        if (curr.next is not null && curr.next.next is not null) {
            curr.next = curr.next.next;
        } else {
            curr.next = null;
        }
        return dummy.next;
    }
}
