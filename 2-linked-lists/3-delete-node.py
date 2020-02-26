from linkedlist import linkedlist


def delete_node(head, val):
    node = head
    while node:
        if node.val != val:
            node = node.next
            continue
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node.val = None
        return node


def test_delete_node():
    head = linkedlist('abcde')
    delete_node(head, 'c')
    assert ''.join(head) == 'abde'
