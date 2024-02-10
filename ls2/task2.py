def intersection_of_lists(list1, list2):
    return list(set(list1).intersection(set(list2)))

list_a = [1, 2, 3, 4, 5, 5]
list_b = [3, 4, 5, 6, 7]
result = intersection_of_lists(list_a, list_b)
print(result)
