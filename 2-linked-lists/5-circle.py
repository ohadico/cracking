from linkedlist import linkedlist


def find_start(head):
    slow = head.next
    fast = head.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def test_circle():
    head = linkedlist('abcde')
    c = None
    node = head
    while node.next:
        if node.val == 'c':
            c = node
        node = node.next
    node.next = c
    assert find_start(head).val == 'c'
