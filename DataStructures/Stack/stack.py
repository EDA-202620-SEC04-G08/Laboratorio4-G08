import DataStructures.List.single_linked_list as sll


def new_stack():
    return sll.new_list()


def push(my_stack, element):
    return sll.add_first(my_stack, element)


def pop(my_stack):
    if sll.is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty')
    else:
        return sll.remove_first(my_stack)


def is_empty(my_stack):
    return sll.is_empty(my_stack)


def top(my_stack):
    if sll.is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty')
    else:
        return sll.get_element(my_stack, 1)


def size(my_stack):
    return sll.size(my_stack)