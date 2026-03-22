'''module Push & BuildOneTwoThree'''
def push(head, data):
    '''creates a new link between nodes'''
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    '''builds a node 1 -> 2 -> 3 -> None'''
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
