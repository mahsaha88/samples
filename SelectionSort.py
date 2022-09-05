def selection_sort(list1):
    for i in range(len(list1)):
        min_idx = i
        for j in range(i+1, len(list1)):
            if list1[min_idx] > list1[j]:
                min_idx = j
        list1[i], list1[min_idx] = list1[min_idx], list1[i]
    return list1


list1 = [23, 34, 98, 56, 76, 33, 12]
print(selection_sort(list1))
