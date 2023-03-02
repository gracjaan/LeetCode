package linked_lists.AddTwoNumbers_2;

import linked_lists.ListNode;

public class SolutionOne {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0, null);
        ListNode pointer = head;
        int addition = 0;

        while (l1 != null || l2 != null || addition == 1){

            int sum = 0;

            if (l1 != null){
                sum += l1.val;
                l1 = l1.next;
            }

            if (l2 != null){
                sum += l2.val;
                l2 = l2.next;
            }

            sum += addition;
            pointer.next = new ListNode(sum % 10);
            pointer = pointer.next;
            addition = sum / 10;

        }
        return head.next;
    }

    public static void main(String[] args) {
        ListNode one = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode two = new ListNode(5, new ListNode(6, new ListNode(4)));

        SolutionOne sol = new SolutionOne();
        ListNode result = sol.addTwoNumbers(one, two);

        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}