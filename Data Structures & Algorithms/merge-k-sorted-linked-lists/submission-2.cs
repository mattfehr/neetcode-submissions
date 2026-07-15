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
    public ListNode MergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode, int> pointers = new PriorityQueue<ListNode, int>();
        foreach (ListNode head in lists) {
            if (head != null) {
                pointers.Enqueue(head, head.val);
            }
        }

        ListNode dummy = new ListNode();
        ListNode curr = dummy;

        while (pointers.Count > 0) {
            ListNode smallest = pointers.Dequeue();

            curr.next = smallest;
            curr = curr.next;

            if (smallest.next is not null) {
                pointers.Enqueue(smallest.next, smallest.next.val);
            }
        }
        return dummy.next;
    }
}
