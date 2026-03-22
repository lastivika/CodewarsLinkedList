'''linked list to string representation'''
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
