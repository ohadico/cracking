def remove_dups(node):
    if node is None:
        return
    head = tail = node
    curr = node.next
    while curr is not None:
        temp = head
        while temp != curr and temp.val != curr.val:
            temp = temp.next
        if temp.val != curr.val:
            tail.next = curr
            tail = tail.next
        curr = curr.next
    tail.next = None
    return head
