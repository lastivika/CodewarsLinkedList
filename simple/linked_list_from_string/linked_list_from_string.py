'''linked list from string'''
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
