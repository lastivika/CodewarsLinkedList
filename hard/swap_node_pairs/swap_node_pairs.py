'''module Swap Node Pairs In Linked List'''
def swap_pairs(head):
    '''swaps each pair of nodes in the list, then returns the head node of the list'''
    if not head:
        return None

    dummy_node = Node(0)
    dummy_node.next = head

    prev = dummy_node # останній вузол зі вже зміненої пари

    while prev.next and prev.next.next:

        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy_node.next
