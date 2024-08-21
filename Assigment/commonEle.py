def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)    
    common_elements_list = list(common_elements)
    return common_elements_list
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_common_elements(list1, list2)
print(result)  
 