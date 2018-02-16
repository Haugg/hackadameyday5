duplicates = [1,1,2,2]

def remove_duplicates(duplicates):
    new_list = []
    for each_element in duplicates:
        if each_element not in new_list:
            new_list.append(each_element)
    return new_list
