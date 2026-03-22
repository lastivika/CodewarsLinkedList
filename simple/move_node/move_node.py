'''module move node'''
class Node(object):
    '''node class'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''context class'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''
    moves a first node from source
    to be the first node in dest
    '''
    if not source:
        raise ValueError
    moved_node = source
    source = source.next

    moved_node.next = dest
    dest = moved_node
    return Context(source, dest)
