from linkedlist import linkedlist


def remove_dups(node):
    if node is None:
        return
    head = prev = node
    curr = node.next
    while curr is not None:
        temp = head
        while temp.val != curr.val:
            temp = temp.next
        if temp != curr:
            curr = curr.next
        else:
            prev.next = curr
            curr = curr.next
            prev = prev.next
    prev.next = None
    return head


def test_remove_dups():
    assert list(remove_dups(linkedlist([1]))) == [1]
    assert list(remove_dups(linkedlist([1, 1]))) == [1]
    assert list(remove_dups(linkedlist(range(5)))) == list(range(5))
    assert list(remove_dups(linkedlist([1, 2, 1, 1, 1, 1]))) == [1, 2]
    assert list(remove_dups(linkedlist([1, 2, 3, 2, 1, 3, 2, 1, 2, 2]))) == [1, 2, 3]
