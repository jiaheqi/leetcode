# leetcode submit region begin(Prohibit modification and deletion)
import unittest


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def create_double_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        cur.next = node
        node.prev = cur
        cur = cur.next
    return head


def print_double_linked_list(head):
    while head:
        print(head.val, end='->')
        head = head.next


if __name__ == '__main__':
    head = create_double_linked_list([1, 2, 3, 4, 5])
    print_double_linked_list(head)
