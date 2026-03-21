'''module get nth'''
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data}, {self.next})"

def get_nth(node, index):
    '''return a node at the index position'''
    if index < 0:
        raise IndexError

    cur = node
    idx = 0
    while cur:
        if idx == index:
            return cur
        cur = cur.next
        idx += 1
    raise IndexError

def test():
    '''test'''
    linked_list = Node(1, Node(2, Node(3, None)))

    result1 = get_nth(linked_list, 1).data
    expected1 = 2
    assert result1 == expected1, f"ERROR TEST 1: expected '{expected1}', got '{result1}'"
    print("test 1: passed")

    result2 = get_nth(linked_list, 2).data
    expected2 = 3
    assert result2 == expected2, f"ERROR TEST 2: expected '{expected2}', got '{result2}'"
    print("test 2: passed")

    try:
        get_nth(linked_list, -1)
        print("ERROR TEST negative: Invalid index value should throw IndexError.")
    except IndexError:
        print("test negative: passed")

    try:
        get_nth(linked_list, 3)
        print("ERROR TEST too big: Invalid index value should throw IndexError.")
    except IndexError:
        print("test too big: passed")

if __name__ == '__main__':
    test()
