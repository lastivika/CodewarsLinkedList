'''module sorted insert'''
def sorted_insert(head, data):
    '''
    inserts a node into the correct location of
    a pre-sorted linked list which is sorted in ascending order
    '''
    n_node = Node(data)
    if not head or data < head.data:
        n_node.next = head
        return n_node

    curr = head
    while curr.next and curr.next.data < data:
        curr = curr.next

    n_node.next = curr.next
    curr.next = n_node

    return head
