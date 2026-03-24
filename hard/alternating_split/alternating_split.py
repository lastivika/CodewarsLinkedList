'''module alternating split'''
class Node(object):
    '''node class'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''class contex'''
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''takes one list and divides up its nodes to make two smaller lists'''
    if not head:
        raise ValueError

    first_head = head
    second_head = head.next if head.next else None

    first_current = first_head
    second_current = second_head
    current = head.next.next if head.next.next else None

    index=0

    while current:
        if index%2==0:
            first_current.next = current
            first_current = current
        else:
            second_current.next = current
            second_current = current

        index += 1
        current = current.next

    first_current.next = None
    second_current.next = None

    return Context(first_head, second_head)
