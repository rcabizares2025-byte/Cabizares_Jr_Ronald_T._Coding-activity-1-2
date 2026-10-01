lst = []
elem_to_remove = {0}

def remove_all_occurrences(lst, elem_to_remove):
    if not lst:
        print("Empty List")
        return

    if not elem_to_remove.intersection(lst):
        print("Not Found")
        return

    new_list = [x for x in lst if x not in elem_to_remove]
    print(new_list)

remove_all_occurrences(lst, elem_to_remove)