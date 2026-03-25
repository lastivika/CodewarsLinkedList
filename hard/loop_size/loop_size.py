'''module loop size'''
def loop_size(node):
    '''returns a loop size'''
    slow = node
    fast = node

    # дивлюсь чи взагалі є цикл
    while slow.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return 0

    fast = fast.next
    length = 1
    while fast != slow:
        fast = fast.next
        length += 1

    return length
