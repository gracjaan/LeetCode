package linked_lists.RemoveNthNodeFromEndOfList_19;

import linked_lists.ListNode;

public class SolutionOne {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null){
            return null;
        }

        int iteration = 0;
        ListNode l1 = head;

        while (l1 != null){
            if (iteration == n-1){
                l1.next = head.next.next;
            }
            l1 = l1.next;
            iteration++;
        }

        return head;
    }

    public ListNode reverseLinkedList (ListNode l1){
        ListNode prev = null;
        ListNode curr = l1;
        ListNode next = l1.next;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public static void main(String[] args) {
        ListNode one = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        SolutionOne sol = new SolutionOne();

        ListNode result = sol.removeNthFromEnd(one, 1);

        while (result != null){
            System.out.println(result.val);
            result = result.next;
        }
    }

}
