from DataStructures.List import array_list as rt
#usar rt para array_list, cambiar push1 a push y top1 a top 
#usar lt para linked_list, cambair push1 a push y top1 a top
def new_stack():
    stacky = rt.new_list()
    return stacky

def push1(my_stack,element):
    if my_stack["size"] == 0:
        my_stack = lt.add_first(my_stack,element)
    else:
        my_stack["last"] = my_stack["first"]
        my_stack = lt.add_first(my_stack,element)
    return my_stack
def push(my_stack,element):
    if my_stack["size"] == 0:
        my_stack = rt.add_first(my_stack,element)
    else:
        
        my_stack = rt.add_first(my_stack,element)
    return my_stack
def pop(my_stack):
    if my_stack["size"] == 0:
        return 'EmptyStructureError: stack is empty'
    else:
        my_stack = rt.remove_first(my_stack)
        return my_stack
def is_empty(my_stack):
    if my_stack["size"] == 0:
        return True
    else:
        return False
    
    
def top1(my_stack):
    if my_stack["size"] == 0:
        return 'EmptyStructureError: stack is empty'
    else:
        return my_stack["first"]["info"]
def size(my_stack):
    return my_stack["size"]
def top(my_stack):
    if my_stack["size"] == 0:
        return 'EmptyStructureError: stack is empty'
    else:
        return rt.first_element(my_stack)
def size(my_stack):
    return my_stack["size"]
