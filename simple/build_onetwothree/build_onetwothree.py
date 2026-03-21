'''module Push & BuildOneTwoThree'''
class Node:
    '''node class'''
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data}, {self.next})"

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


if __name__ == '__main__':
    print(build_one_two_three())
