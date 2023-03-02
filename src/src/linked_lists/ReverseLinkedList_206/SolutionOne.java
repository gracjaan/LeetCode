package linked_lists.ReverseLinkedList_206;

import linked_lists.ListNode;

public class SolutionOne {

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
        ListNode one = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode two = new ListNode(5, new ListNode(6, new ListNode(4)));

        SolutionOne sol = new SolutionOne();
        ListNode pre = sol.reverseLinkedList(one);

        while (pre != null) {
            System.out.println(pre.val);
            pre = pre.next;
        }
    }
}
