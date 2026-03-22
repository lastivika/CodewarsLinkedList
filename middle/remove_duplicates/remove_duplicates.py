''' module remove duplicates'''
class Node(object):
    '''class node'''
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''removes duplicates from linked list'''
    if not head:
        return None

    curr = head
    while curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
