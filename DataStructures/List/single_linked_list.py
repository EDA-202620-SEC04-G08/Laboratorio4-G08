from DataStructures.List import list_node as ln

def new_list():
    new_list = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return new_list
def get_element(my_list,pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos :
        node = node["next"]
        searchpos += 1
    return node["info"]
def is_present(my_list,element,cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count 
def add_first(my_list,element):
    my_list["size"] += 1
    new = ln.new_single_node(element)
    if my_list["first"] == None:
        my_list["first"] = new
        my_list["last"] = new
    else:
     new["next"] = my_list["first"]
     my_list["first"] = new

def add_last(my_list,element):
    
    new = ln.new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = new
        my_list["last"] = new
    else:
        my_list["last"]["next"] = new
    my_list["size"] += 1
    return my_list
        
def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return["first"]
    
def last_element(my_list):
    return["last"]
        
from DataStructures.List import list_node as lt

def new_list():
    new_list = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return new_list
def is_present(my_list,element,cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count 
    
def remove_first(my_list):
            if my_list["size"] == 0:
                return my_list
            current = my_list["first"]
            informacion = current["info"]
            elemento = my_list["first"]["info"]
            if my_list["size"] == 1:
                my_list["first"] = None
                my_list["last"] = None
                my_list["size"] -= 1
            else:
                my_list["first"] = my_list["first"]["next"]
                my_list["first"] = current["next"]
                my_list["size"] -= 1
            return informacion
        
def remove_last(my_list):
    if my_list["size"] == 0:
        return my_list
    else:
        removed_elm = my_list["last"]["info"]
        element = my_list["last"]["info"]
        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
        else:
            rec = my_list["first"]
            while rec["next"] != my_list["last"]:
                rec = rec["next"]
            my_list["last"] = rec
        my_list["size"] -= 1
        return removed_elm
    
def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("list index out of range")

    new_node = {"info": element, "next": None}

    if pos == 0:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
        if my_list["size"] == 0:
            my_list["last"] = new_node
    else:
        prev = my_list["first"]
        for i in range(pos - 1):
            prev = prev["next"]
        new_node["next"] = prev["next"]
        prev["next"] = new_node
        if pos == my_list["size"]:
            my_list["last"] = new_node

    my_list["size"] += 1
    return my_list
def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return IndexError("list index out of range")

    if pos == 0:
        removed_node = my_list["first"]
        my_list["first"] = None
        if my_list["size"] == 1:
            my_list["last"] = None

    else:
        prev = my_list["first"]
        for i in range(pos - 1):
            prev = prev["next"]
        removed_node = prev["next"]
        prev["next"] = removed_node["next"]
        if pos == my_list["size"] - 1:
            my_list["last"] = prev

    my_list["size"] -= 1
    return removed_node

def change_info(my_list, pos, new_info):
    if pos < 0 or pos > my_list["size"]:
        return IndexError("list index out of range")
    current = my_list["first"]
    for i in range(pos):
        current = current["next"]
        my_list[current]["info"] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"] or pos2 < 0 or pos2 >= my_list["size"]:
        return IndexError("list index out of range")
    current1 = my_list["first"]
    for i in range(pos1):
        current1 = current1["next"]
    current2 = my_list["first"]
    for i in range(pos2):
        current2 = current2["next"]
    temp = current1["info"]
    current1["info"] = current2["info"]
    current2["info"] = temp
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list["size"] or num_elements < 0:
        return IndexError("list index out of range")
    current = my_list["first"]
    for e in range(pos):
        current = current["next"]
    sub_lista = new_list()   
    for i in range(pos, my_list["size"]):
        add_first(sub_lista, current)
        current = current["next"]
    return sub_lista        
        
        
    
        