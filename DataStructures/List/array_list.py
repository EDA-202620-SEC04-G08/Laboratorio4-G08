

def new_list():
    new_list = {
        "elements": [],
        "size": 0,
    }
    return new_list

def add_first(my_list,element):
    my_list["size"] += 1
    if my_list["size"] != 0:
       my_list["elements"].insert(0,element)
    else:
       my_list["elements"].append(element)
    return my_list
    



def add_last(my_list,element):
    my_list["size"] += 1
    my_list["elements"].append(element)
    return my_list

     
def size(my_list):
    return my_list["size"]
    
    
def first_element(my_list):
    return my_list["elements"][0]

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False

def last_element(my_list):
    if is_empty(my_list):
       raise Exception('IndexError: list index out of range')
    else:
        return my_list["elements"][size(my_list) - 1]

def delete_element(my_list, pos):
    if 0 <= pos < size(my_list):
        my_list["elements"].pop(pos)
    else:
        raise Exception('IndexError: list index out of range')
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')

    my_list["size"] -= 1
    return my_list["elements"].pop(0)
    

def remove_last(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')

    my_list["size"] -= 1
    return my_list["elements"].pop()
    

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif is_empty(my_list):
        my_list["elements"].append(element)
    else:
        my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else: 
        my_list["elements"][pos] = new_info
        return my_list
    

def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list)):
        raise Exception('IndexError: list index out of range')
    else:
        x = my_list["elements"][pos_2]
        my_list["elements"][pos_2] = my_list["elements"][pos_1]
        my_list["elements"][pos_1] = x
        return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"]:
        raise Exception('IndexError: list index out of range')

    new_elements = my_list["elements"][pos_i:pos_i + num_elements]

    return {
        "elements": new_elements,
        "size": len(new_elements)
    }
    
def get_element(my_list, pos):
    size = my_list["size"]
    if size < pos or pos <= 0:
        return IndexError
    return my_list["elements"][pos]

def is_present(my_list, element, cpm_function):
    size = my_list["size"]
    encontrado = False
    i = 0
    if size == 0:
        return -1
    while i < size:
        if cpm_function(my_list["elements"][i], element) == 0:
            return 1
        i += 1
    return -1