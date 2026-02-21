from DataStructures.List import array_list as lt

def new_queue():
    queue = lt.new_list()
    return queue

def enqueue(my_queue, element):
    return lt.add_last(my_queue, element)

def dequeue(my_queue):
    if lt.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    else:
        x = lt.first_element(my_queue)
        lt.remove_first(my_queue)
        return x

def peek(my_queue):
    if lt.is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    else:
        return lt.first_element(my_queue)

def is_empty(my_queue):
    return lt.is_empty(my_queue)

def size(my_queue):
    return lt.size(my_queue)

