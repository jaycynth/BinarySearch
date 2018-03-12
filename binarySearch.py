# iterative implementation of binary search in Python


def binary_search(a_list, item):
    
    first = 0
    last = len(a_list) - 1

    while first <= last:
        i = int((first + last) / 2)

        if a_list[i] == item:
            return '{item} found at position {i}'.format(item=item, i=i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            return '{item} not found in the list'.format(item=item)
a=[2,3,5,66,78,9]
print(binary_search(a,5))


# recursive implementation of binary search in Python


def binary_search_recursive(a_list, item):
    

    first = 0
    last = len(a_list) - 1

    if len(a_list) == 0:
        return '{item} was not found in the list'.format(item=item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return '{item} found'.format(item=item)
        else:
            if a_list[i] < item:
                return binary_search_recursive(a_list[i+1:], item)
            else:
                return binary_search_recursive(a_list[:i], item)
a=[2,3,5,66,78,9]
print(binary_search(a,5))
