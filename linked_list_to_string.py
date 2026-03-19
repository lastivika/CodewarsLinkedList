'''linked list to string representation'''
class Node():
    '''linked list'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    '''
    accepts a list and
    returns a string representation of the list
    '''
    res = []
    while node is not None:
        res.append(str(node.data))
        node = node.next
    res.append('None')
    return ' -> '.join(res)

def test():
    '''testing'''
    # test1
    result1 = stringify(Node(0, Node(1, Node(2, Node(3)))))
    expected1 = '0 -> 1 -> 2 -> 3 -> None'
    assert result1 == expected1, f"ERROR TEST 1: expected '{expected1}', got '{result1}'"
    print("test 1: passed")

    # test2
    result2 = stringify(None)
    expected2 = 'None'
    assert result2 == expected2, f"ERROR TEST 2: expected '{expected2}', got '{result2}'"
    print("test 2: passed")

    # test3
    result3 = stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
    expected3 = '0 -> 1 -> 4 -> 9 -> 16 -> None'
    assert result3 == expected3, f"ERROR TEST 3: expected '{expected3}', got '{result3}'"
    print("test 3: passed")

if __name__ == '__main__':
    test()
