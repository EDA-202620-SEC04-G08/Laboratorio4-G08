from DataStructures.List import array_list as lt

def new_queue ():
    queue = lt.new_list()
    return queue

def enqueue(my_queue, element):
    lt.add_last(my_queue, element)
    return my_queue

def dequeue(my_queue):
    if lt.size(my_queue) > 0:
        primer_elemento = lt.first_element(my_queue)
        lt.delete_element(my_queue,0)
    else:
        raise Exception('EmptyStructureError: queue is empty')
    return primer_elemento

def is_empty(my_queue):
    vacio = lt.is_empty(my_queue)
    return vacio

def peek (my_queue):
    if lt.size(my_queue) > 0:
        primer_elemento = lt.first_element(my_queue)
    else:
        raise Exception('EmptyStructureError: queue is empty')
    return primer_elemento

def size (my_queue):
    size = lt.size(my_queue)
    return size
