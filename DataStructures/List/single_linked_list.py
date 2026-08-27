import DataStructures.List.list_node as ln

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }

    return newlist


def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]


def is_present(my_list, element, cnp_function):
    is_in_array = False
    temp = my_list["first"]
    count =0
    while not is_in_array and temp is not None:
        if cnp_function(element ,temp["info"] ) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        return count - 1
    return count


def add_first(my_list, element):
    nuevo_nodo = {"info": element,
                "next": my_list["first"]
                }
    my_list["first"] = nuevo_nodo
    if my_list["size"] == 0:
        my_list["last"] = nuevo_nodo
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    nuevo_nodo = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = nuevo_nodo
    else:
        my_list["last"]["next"] = nuevo_nodo
    my_list["last"] = nuevo_nodo
    my_list["size"] += 1
    return my_list


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    if my_list["first"] is not None:
        return my_list["first"]["info"]
    return None


def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False


def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]


def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    elif my_list["size"] > 0:

        searchpos = 0
        node = my_list["first"]
        prev = my_list["first"]
        
        while searchpos <pos:
            prev = node
            node = node["next"]
            searchpos += 1
        prev["next"] = node["next"]
        my_list["size"] -=1

    
    return my_list


def remove_first(my_list):

    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')

    node = my_list["first"]

    if my_list["size"] > 0:
        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
            my_list["size"] = 0

        else:
            my_list["first"]=node["next"]
            my_list["size"] -= 1
    return node["info"]


def remove_last(my_list):

    if is_empty(my_list):
            raise Exception('IndexError: list index out of range')

    last = my_list["last"]

    if my_list["size"] > 0:

        searchpos = 0
        node = my_list["first"]
        
        while searchpos < my_list["size"]-2:
            node = node["next"]
            searchpos += 1
            
        node["next"] = None
        my_list["last"]=node
        my_list["size"]-=1
    return last["info"]


def insert_element(my_list, element, pos):

    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    newnode = ln.new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["last"] = newnode
        my_list["first"] = newnode
        my_list["size"]+=1

    elif my_list["size"] > 0:

        searchpos = 0
        node = my_list["first"]
        prev = my_list["first"]
        
        while searchpos <=pos:
            prev = node
            node = node["next"]
            searchpos += 1
        newnode["next"] = node
        prev["next"] = newnode
        my_list["size"] +=1
    
    return my_list


def change_info(my_list, pos, new_info):

    if pos < 0 or pos > size(my_list):
            raise Exception('IndexError: list index out of range')

    elif my_list["size"] == 0:
        if pos == 0:
            newnode = ln.new_single_node(new_info)    
            my_list["first"] = newnode
            my_list["last"] = newnode
            my_list["sizea"] = 1
    elif my_list["size"] > 0:
        searchpos = 0
        node = my_list["first"]
        
        while searchpos < pos:
            
            node = node["next"]
            searchpos += 1
        node["info"] = new_info
    
    return my_list


def exchange(my_list, pos1, pos2):

    if pos1 < 0 or pos1 > size(my_list) or pos2 < 0 or pos2 > size(my_list):
            raise Exception('IndexError: list index out of range')

    elif my_list["size"] > 0:

        el1=get_element(my_list, pos1)
        el2=get_element(my_list, pos2)
        change_info(my_list, pos1, el2)
        change_info(my_list, pos2, el1)
    return my_list


def sub_list(my_list, pos, num_elements):
    sublist = new_list()
    if pos<0 or pos>=my_list["size"]:
        raise Exception('IndexError: list index out of range')
    
    elif my_list["size"] > 0:
        searchpos=0
        node = my_list["first"]

        while searchpos < pos:
            node = node["next"]
            searchpos += 1

        sublist["first"] = node
        searchpos=0
        node = sublist["first"]

        while searchpos < num_elements:
            node = node["next"]
            searchpos += 1
        node["next"] = None
        sublist["last"] = node
        sublist["size"] = num_elements
    
    return sublist