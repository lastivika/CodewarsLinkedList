'''linked list from string'''
class Node:
    '''node class'''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __eq__(self, other):
        return self.data == other.data and self.next == other.next

    def __repr__(self):
        return f"Node({self.data}, {self.next})"


def linked_list_from_string(list_repr: str) -> Node | None:
    '''returns a linked list from string'''
    nodes_in_list = list_repr.split(" -> ")

    if nodes_in_list[-1] == 'None':
        nodes_in_list = nodes_in_list[:-1]
    if not nodes_in_list:
        return None

    head = Node(int(nodes_in_list[0]))
    curr_node = head
    for node in nodes_in_list[1:]:
        curr_node.next = Node(int(node))
        curr_node = curr_node.next

    return head


def test():
    '''test'''
    result1 = linked_list_from_string("1 -> 2 -> 3 -> None")
    expected1 = Node(1, Node(2, Node(3)))
    assert result1 == expected1, f"ERROR TEST 1: expected '{expected1}', got '{result1}'"
    print("test 1: passed")

    result2 = linked_list_from_string("0 -> 1 -> 4 -> 9 -> 16 -> None")
    expected2 = Node(0, Node(1, Node(4, Node(9, Node(16)))))
    assert result2 == expected2, f"ERROR TEST 2: expected '{expected2}', got '{result2}'"
    print("test 2: passed")

    result3 = linked_list_from_string("None")
    expected3 = None
    assert result2 == expected2, f"ERROR TEST 3: expected '{expected3}', got '{result3}'"
    print("test 3: passed")

if __name__ == '__main__':
    test()
