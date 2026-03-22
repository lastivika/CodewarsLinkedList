'''module get nth'''
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

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
